from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from shortener.models import URL
from django.contrib import messages
from django.conf import settings


@login_required()
def index(request):
    if request.method == 'POST':
        try:
            # assert request.method == 'POST', 'Invalid request!'
            assert request.POST.get('short_code', None), 'Short code not provided.'
            if request.POST.get('website_url', None):
                full_url = request.POST.get('website_url')
                url_hash = request.POST.get('short_code')
                assert not URL.objects.filter(url_hash__iexact=url_hash), 'Short code already exists!'
                assert not URL.objects.filter(full_url__iexact=full_url), 'URL already exists!'
                short_url = URL.objects.create(full_url=full_url, url_hash=url_hash)
            elif request.FILES:
                print(request.FILES.get('file_upload'))
                url_hash = request.POST.get('short_code')
                assert not URL.objects.filter(url_hash__iexact=url_hash), 'Short code already exists!'
                short_url = URL.objects.create(url_hash=url_hash, file_path=request.FILES.get('file_upload'))
            else:
                messages.error(request, 'Something went wrong.')
                return redirect('index')

            return render(request, 'shortener/your_url.html', {
                'short_url': '%s://%s/%s' % (request.scheme, request.get_host(), short_url.url_hash)
            })
        except Exception as e:
            messages.error(request, '%s' % e)
            return redirect('index')
    else:
        return render(request, 'shortener/index.html')


def redirect_to(request, short_code):
    short_url_object = URL.objects.filter(url_hash=short_code).first()
    if short_url_object:
        short_url_object.clicks += 1
        short_url_object.save()
        if short_url_object.full_url:
            redirect_url = short_url_object.full_url
        else:
            redirect_url = '%s://%s%s%s' % (request.scheme, request.get_host(),
                                            settings.MEDIA_URL, short_url_object.file_path)
        return redirect(redirect_url)
    else:
        return render(request, '404.html', status=404)
