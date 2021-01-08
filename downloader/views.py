from django.shortcuts import render, redirect
from django.http import HttpResponse

from .wrapper import YouTubeWrapper, StreamTemplate

from pytube import exceptions

# Create your views here.

def home(request, error_message=None):
    context = {}

    if(error_message):
        context['message'] = error_message

    return render(request, 'downloader/home.html', context)

def process(request):
    link = request.POST['link']
    error_message = ''

    try:
        youtube = YouTubeWrapper(link)

        return render(request, 'downloader/done.html', {'video' : youtube})

    except exceptions.RegexMatchError:
        error_message='Please Enter a valid link'
    except exceptions.ExtractError:
        error_message = "The Video you are trying to download doesn't exist"
    except exceptions.VideoUnavailable:
        error_message = 'The Video is not available'

    return HttpResponse(error_message)

def done(request):
    return HttpResponse('Done')

def on_complete(stream, file_path):
    pass
