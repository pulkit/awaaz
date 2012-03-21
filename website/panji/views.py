from django.shortcuts import render_to_response,get_object_or_404
from news.models import yourvoice,ScrollNews
from django.core.paginator import Paginator,InvalidPage,EmptyPage
from django.template import RequestContext


def panji_page(request):
    context = RequestContext(request)
    scroll_list=ScrollNews.objects.all().order_by('-id')[:6]
    panji_list=panji.objects.all().order_by('-id')[:6]
    return render_to_response('awaaz/panji.html',{'panji_list':panji_list,'scroll_list':scroll_list},context_instance = context)
