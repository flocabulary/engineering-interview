from django.shortcuts import render
from django.shortcuts import redirect
from url_rest.models import UrlShort
from django.template import loader

def index(request):
    template = loader.get_template('url_front/index.html')
    context = { }
    return render(request, 'url_front/index.html', context)

def go_short_url(requests, short_url):
    url = UrlShort.from_short_url(short_url)
    return redirect(url.url)