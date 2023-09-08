from django.views.generic import DetailView

from main.models import *


class Page(DetailView):
    model = Page
    template_name = 'main/page.html'
    context_object_name = 'page'

    def get_object(self, queryset=None):
        if self.kwargs.get(self.slug_url_kwarg):
            return super().get_object(queryset)
        else:
            return self.model.objects.get(is_homepage=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
