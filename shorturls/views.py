from django.shortcuts import render, redirect, get_object_or_404
from .models import ShortUrl

def shorter(request):
    if request.method=="POST":
        url = request.POST.get('url')
        ShortUrl.objects.get_or_create(original_url=url, user=request.user)
        return redirect('shorter')

    urls = ShortUrl.objects.filter(user=request.user)
    context = {
        'urls': urls
    }
    return render(request, 'shorturl/shorter.html', context)

def redirecter(request, short_code):
    url_obj = get_object_or_404(ShortUrl, short_url=short_code)
    return redirect(url_obj.original_url)

def deleteUrl(request, pk):
    ShortUrl.objects.filter(id=pk).delete()
    return redirect('shorter')
