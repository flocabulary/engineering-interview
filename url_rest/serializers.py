from rest_framework import serializers

from url_rest.models import UrlShort

class UrlShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = UrlShort
        fields = ('id', 'title', 'description', 'url', 'short_url')
