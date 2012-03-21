from django.template import RequestContext
from django.shortcuts import render_to_response

from videos.models import *
from photologue.models import Photo

def video_gallery(request):
    context = RequestContext(request)
    all_videos = video.objects.all()
    category = Category.objects.all()
    return render_to_response('awaaz/video_gallery.html',{'videos':all_videos,'categories':category},context_instance = context)

def video_content(request):
    context = RequestContext(request)
    pk = request.GET.get('pk',False)
    current_video = video.objects.get(id = pk)
    return render_to_response('awaaz/video.html',{'video':current_video},context_instance = context)

def coming_soon(request):
    context = RequestContext(request)
    return render_to_response('awaaz/coming_soon.html',context_instance = context)

def video_category(request):
    context = RequestContext(request)
    category_get = request.GET.get('category',False)
    videos = video.objects.filter(category__name = category_get)
    return render_to_response('awaaz/video_category.html',{'videos':videos},context_instance = context)


