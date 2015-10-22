from django.views.generic import TemplateView

import apbdb.gamedb.models as models


class achievement_list(TemplateView):
    template_name = "achievements.html"

    def get_context_data(self, **kwargs):
        context = super(achievement_list, self).get_context_data(**kwargs)

        faction_arg = self.request.GET.get("faction", None)

        context['achievements'] = models.Playerroles.objects.filter(bachievement=1).order_by('sdisplayname')
        context['factions'] = models.Factions.objects.exclude(espawnzonemarker=0)

        if faction_arg:
            context['faction'] = context['factions'].get(sapbdb=faction_arg)
            context['achievements'] = context['achievements'].filter(efaction=context['faction'])
        else:
            context['faction'] = None

        return context