from django.db import models
from django.urls import reverse_lazy


class Menu(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, unique=True, db_index=True)

    def get_absolute_url(self):
        return reverse_lazy('home', kwargs={'slug': self.slug})
