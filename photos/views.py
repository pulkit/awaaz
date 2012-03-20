# Create your views here.
from django.shortcuts import render_to_response
from news.models import ScrollNews

def photo(request):
    scroll_list=ScrollNews.objects.all().order_by('-id')[:6]
    return render_to_response('awaaz/photos.html',{'scroll_list':scroll_list})
