from url_rest.models import UrlShort
from url_rest.serializers import UrlShortSerializer
from rest_framework import generics

# Create your views here.
class UrlShortList(generics.ListCreateAPIView):
    queryset = UrlShort.objects.all()
    serializer_class = UrlShortSerializer

class UrlShortDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UrlShort.objects.all()
    serializer_class = UrlShortSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'urls': reverse('url-list', request=request, format=format)
    })

from rest_framework import renderers
from django.shortcuts import redirect

class UrlShortGo(generics.GenericAPIView):
    queryset = UrlShort.objects.all()
    renderer_classes = (renderers.StaticHTMLRenderer,)

    def get(self, request, *args, **kwargs):
        url = self.get_object()
        return redirect(url.url)