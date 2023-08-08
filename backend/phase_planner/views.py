from django.views.generic import TemplateView, ListView, DetailView
from .models import To_Do, Phase, Project, Reward
from django.shortcuts import redirect


class BaseView(TemplateView):
    template_name = "base.html"


class PhaseListView(ListView):
    model = Phase
    # template_name = "phase_list.html"
    context_object_name = 'object_list'


class PhaseDetailView(DetailView):
    model = Phase
    # template_name = "phase_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = Phase.objects.all()
        return context


def cross_off(request, to_do_id):
    item = To_Do.objects.get(pk=to_do_id)
    item.to_do_is_done = True
    item.save()
    # Get the referring URL from the request
    referring_url = request.META.get('HTTP_REFERER')

    # Redirect the user back to the referring URL
    return redirect(referring_url)


def uncross(request, to_do_id):
    item = To_Do.objects.get(pk=to_do_id)
    item.to_do_is_done = False
    item.save()
    # Get the referring URL from the request
    referring_url = request.META.get('HTTP_REFERER')
    # Redirect the user back to the referring URL
    return redirect(referring_url)
