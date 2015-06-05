from haystack import indexes
import models


class IndividualIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    first_name = indexes.CharField(model_attr='first_name')
    middle_name = indexes.CharField(model_attr='middle_name')
    last_name = indexes.CharField(model_attr='last_name')

    def get_model(self):
        return models.Individual

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()

