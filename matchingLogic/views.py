from django.shortcuts import render
from haystack.query import SearchQuerySet
# Create your views here.
from django.http import HttpResponse

import models


def name_filter(first, middle, last):
    r = SearchQuerySet()
    for text in first:
        r = r.filter(first_name=text)
        if '-' in text:
            for target in text.split('-'):
                r = r.filter_or(first_name=target)
    for text in middle:
        r = r.filter(middle_name=text)
        if '-' in text:
            for target in text.split('-'):
                r = r.filter_or(middle_name=target)
    for text in last:
        r = r.filter(last_name=text)
        if '-' in text:
            for target in text.split('-'):
                r = r.filter_or(last_name=target)
    return r


def index(request):
    if request.GET.__len__() == 0:
        return render(request, 'matchingLogic/index.html')
    first = request.GET['first'].split()
    middle = request.GET['middle'].split()
    last = request.GET['last'].split()
    if len(first)+len(middle)+len(last) == 0:
        return render(request, 'matchingLogic/index.html')
    r = name_filter(first, middle, last)
    if r.count() == 0:
        print 'oops!'
        middle = [m[0] for m in middle]
        r = name_filter(first, middle, last)
    results = []
    for entry in r:
        results.append({'score': entry.score, 'name': entry.text})
    full_name = '{} {} {}'.format(request.GET['first'], request.GET['middle'],
                                  request.GET['last'])
    context = {'people': results, 'target_name': full_name,
               'first': request.GET['first'], 'middle': request.GET['middle'],
               'last': request.GET['last']}
    return render(request, 'matchingLogic/index.html', context)

def person(request, individual_id):
    return HttpResponse("Looking at individual {}".format(individual_id))
