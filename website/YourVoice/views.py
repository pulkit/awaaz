from django.shortcuts import render_to_response,get_object_or_404
from django.core.paginator import Paginator,InvalidPage,EmptyPage
from django.template import RequestContext



#def YourVoice(request):
    #context = RequestContext(request)
    #paginator=Paginator(article_list,5)
    #try:
        #page = int(request.GET.get('page', '1'))
    #except ValueError:
        #page = 1
    #try:
        #articles = paginator.page(page)
    #except (EmptyPage, InvalidPage):
        #articles = paginator.page(paginator.num_pages)
    #return render_to_response('awaaz/yv.html',context_instance = context)


#def article_topic(request, article_id):
    #context = RequestContext(request)
    #try:
        #p = yourvoice.objects.get(pk=article_id)
    #except yourvoice.DoesNotExist:
        #raise Http404
    #return render_to_response('awaaz/article_topic.html', {'topic': p},context_instance = context)
