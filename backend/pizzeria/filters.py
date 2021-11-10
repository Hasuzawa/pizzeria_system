from django.contrib.admin import SimpleListFilter



class OccurenceFilter(SimpleListFilter):
    title = "times ordered"
    parameter_name = "occurence"
    
    def lookups(self, request, model_admin):
        pass