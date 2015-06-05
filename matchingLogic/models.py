from django.db import models


# Create your models here.
class Individual(models.Model):
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateTimeField('birth date', blank=True, null=True)

    def __unicode__(self):
        return '{} {} {}'.format(self.first_name, self.middle_name,
                                 self.last_name)

    def has_extra_data(self):
        return models.ExtraData.objects.filter(individual_id=self.pk).exists()

    def full_name(self):
        return '{} {} {}'.format(self.first_name, self.middle_name,
                                 self.last_name)

class ExtraData(models.Model):
    individual_id = models.ForeignKey(Individual)
    text = models.TextField()

    def __unicode__(self):
        return 'Extra data for {} {} {}'.format(self.individual_id.first_name,
                                                self.individual_id.middle_name,
                                                self.individual_id.last_name)
