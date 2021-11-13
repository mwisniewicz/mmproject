from django.views.generic.base import TemplateView


class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['test'] = 'Hej'
        context['test2'] = 'Hej2'
        context['test3'] = 'Hej3'
        return context