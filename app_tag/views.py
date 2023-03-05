from django.urls import reverse_lazy
from django.views.generic.base import TemplateView


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_absolute_url(self):
        return reverse_lazy('home', kwargs={'slug': self.slug})

