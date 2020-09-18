from django.shortcuts import render, redirect
from .models import short_urls
from .forms import UrlForm
from .shortener import shortener
from django.core.paginator import Paginator

# Create your views here.

def Home(request, token):
    url = short_urls.objects.filter(short_url=token)[0]
    return redirect(url.long_url)


def Make(request):
    form = UrlForm(request.POST or None)
    url = ''
    is_error = False
    if request.method == 'POST':
        if form.is_valid():
            newUrl = form.save()
            url = shortener().issue_token()
            newUrl.short_url = url
            newUrl.save()
            return redirect("/records")
        else:
            form = UrlForm()
            is_error = True
            url = "Entered URL exists in our records... Please check records tab."
    return render(request, 'home.html', {'form': form, 'url': url, 'is_error': is_error})


def Records(request):
    host = request.headers['Host']
    urls = short_urls.objects.all()
    paginator = Paginator(urls, 8)
    page = request.GET.get('page')
    urls = paginator.get_page(page)
    return render(request, 'records.html', {'urls': urls, 'host': host})


def About(request):
    return render(request, 'about.html', {'name': 'Arun'})
