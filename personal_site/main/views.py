from django.views.generic import ListView

from main.models import *


class Contacts(ListView):
    model = Block
    template_name = 'main/contacts.html'
    context_object_name = 'blocks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['settings'] = Settings.objects.first()

        return context
