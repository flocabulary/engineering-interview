from django.db import models
from url_converter import converter

class UrlShort(models.Model):
    created = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=80, blank=True, default='')
    description = models.CharField(max_length=200, blank=True, default='')
    url = models.TextField()

    @property
    def short_url(self):
        c = converter.CharConverter()
        return c.encode(self.pk)

    # better to use Custom Manager
    # https://docs.djangoproject.com/en/dev/topics/db/managers/#custom-managers
    @staticmethod
    def from_short_url(url_short):
        c = converter.CharConverter()
        pk = c.decode(url_short)
        return UrlShort.objects.get(pk=pk)

    class Meta:
        ordering = ('created',)
