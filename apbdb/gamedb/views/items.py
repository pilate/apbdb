from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView

import apbdb.gamedb.models as models


class detail(TemplateView):
    template_name = "items/detail.html"

    def get_context_data(self, **kwargs):
        context = super(detail, self).get_context_data(**kwargs)
        context['item'] = get_object_or_404(models.Inventoryitemtypes, sapbdb=kwargs['item'])
        return context
