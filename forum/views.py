from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Message


def forum(request):
    messages = Message.objects.order_by('created_at')
    context = {
        'messages': messages,
    }

    return render(request, 'forum/forum.html', context)

def send(request):
    if request.method=='POST':
        text = request.POST.get('text')
        if text:
            Message.objects.create(text = text, user=request.user)
    return redirect('forum')

