# Create your views here.
from django.shortcuts import render_to_response,get_object_or_404
from news.models import MainNews , Institute,Gymkhana,External,yourvoice,ScrollNews,panji
from django.http import Http404
from django.core.paginator import Paginator,InvalidPage,EmptyPage
from django.template import RequestContext

def display_news(request):
    context = RequestContext(request)
    news_list=MainNews.objects.all().order_by('-date')[:4]
    insti_list=Institute.objects.all().order_by('-id')[:4]
    gym_list=Gymkhana.objects.all().order_by('-id')[:4]
    ext_list=External.objects.all().order_by('-id')[:4]
    scroll_list=ScrollNews.objects.all().order_by('-id')[:6]
    return render_to_response('awaaz/base.html',{
        'news_list':news_list,
        'insti_list':insti_list,
        'gym_list':gym_list,
        'ext_list':ext_list,
        'scroll_list':scroll_list
        },context_instance = context)	   




def about(request):
    context = RequestContext(request)
    scroll_list=ScrollNews.objects.all().order_by('-id')[:6]
    return render_to_response('awaaz/abt.html',{'scroll_list':scroll_list},context_instance = context)

def contact(request):
    context = RequestContext(request)
    scroll_list=ScrollNews.objects.all().order_by('-id')[:6]
    return render_to_response('awaaz/cnt.html',{'scroll_list':scroll_list},context_instance = context)

def gymkhana(request):
    context = RequestContext(request)
    scroll_list=ScrollNews.objects.all().order_by('-id')[:6]
    return render_to_response('awaaz/gym.html',{'scroll_list':scroll_list},context_instance = context)

def issues(request):
    context = RequestContext(request)
    scroll_list=ScrollNews.objects.all().order_by('-id')[:6]
    return render_to_response('awaaz/isu.html',{'scroll_list':scroll_list},context_instance = context)

def sponsors(request):
    context = RequestContext(request)
    scroll_list=ScrollNews.objects.all().order_by('-id')[:6]
    return render_to_response('awaaz/sponsors.html',{'scroll_list':scroll_list},context_instance = context)

def YourVoice(request):
    context = RequestContext(request)
    article_list=yourvoice.objects.all().order_by('-date')
    scroll_list=ScrollNews.objects.all().order_by('-id')
    paginator=Paginator(article_list,5)
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    try:
        articles = paginator.page(page)
    except (EmptyPage, InvalidPage):
        articles = paginator.page(paginator.num_pages)
    return render_to_response('awaaz/yv.html',{'articles':articles,'scroll_list':scroll_list},context_instance = context)

def news_topic(request, news_id):
    context = RequestContext(request)
    scroll_list=ScrollNews.objects.all().order_by('-id')[:6]
    try:
        p = MainNews.objects.get(pk=news_id)
    except MainNews.DoesNotExist:
        raise Http404
    return render_to_response('awaaz/topic.html', {'topic': p,'scroll_list':scroll_list},context_instance = context)


def about_gym(request):
    context = RequestContext(request)
    scroll_list=ScrollNews.objects.all().order_by('-id')[:6]
    return render_to_response('awaaz/aboutgym.html',{'scroll_list':scroll_list},context_instance = context)

def postbearers(request):
    context = RequestContext(request)
    scroll_list=ScrollNews.objects.all().order_by('-id')[:6]
    return render_to_response('awaaz/postbearers.html',{'scroll_list':scroll_list},context_instance = context)

def gym_cal(request):
    context = RequestContext(request)
    scroll_list=ScrollNews.objects.all().order_by('-id')[:6]
    return render_to_response('awaaz/gymcal.html',{'scroll_list':scroll_list},context_instance = context)

def all_news(request):
    context = RequestContext(request)
    scroll_list=ScrollNews.objects.all().order_by('-id')[:6]
    news_list=MainNews.objects.all().order_by('-date')
    paginator=Paginator(news_list,5)
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    try:
        news = paginator.page(page)
    except (EmptyPage, InvalidPage):
        news = paginator.page(paginator.num_pages)
    return render_to_response('awaaz/allnews.html',{'news':news,'scroll_list':scroll_list},context_instance = context)

def article_topic(request, article_id):
    context = RequestContext(request)
    scroll_list=ScrollNews.objects.all().order_by('-id')[:6]
    try:
        p = yourvoice.objects.get(pk=article_id)
    except yourvoice.DoesNotExist:
        raise Http404
    return render_to_response('awaaz/article_topic.html', {'topic': p,'scroll_list':scroll_list},context_instance = context)

def panji_page(request):
    context = RequestContext(request)
    scroll_list=ScrollNews.objects.all().order_by('-id')[:6]
    panji_list=panji.objects.all().order_by('-id')[:6]
    return render_to_response('awaaz/panji.html',{'panji_list':panji_list,'scroll_list':scroll_list},context_instance = context)
