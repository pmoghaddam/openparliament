from haystack import site
from haystack import indexes

from parliament.core.models import Politician
from parliament.search.index import SearchIndex

class PolIndex(SearchIndex):
    text = indexes.CharField(document=True, use_template=True)
    boosted = indexes.CharField(use_template=True, stored=False)
    politician = indexes.CharField(model_attr='name', indexed=False)
    party = indexes.CharField(model_attr='latest_member__party__short_name')
    province = indexes.CharField(model_attr='latest_member__riding__province')
    url = indexes.CharField(model_attr='get_absolute_url', indexed=False)
    doctype = indexes.CharField(default='mp')
    
    def get_queryset(self):
        return Politician.objects.elected()

    def should_obj_be_indexed(self, obj):
        # Currently used only in live updates, not batch indexing
        return bool(obj.latest_member)


site.register(Politician, PolIndex)
