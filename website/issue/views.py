# Create your views here.
from issue.models import issue
from django.shortcuts import render_to_response, get_object_or_404
from django.http import Http404
from django.template import RequestContext
from django.core.paginator import Paginator,InvalidPage,EmptyPage

def show_issue(request):
    issue_list=issue.objects.all().order_by('-id')
    paginator=Paginator(issue_list,4)
    try:
            page = int(request.GET.get('page', '1'))
    except ValueError:
            page = 1
    try:
            issues = paginator.page(page)
    except (EmptyPage, InvalidPage):
            issues = paginator.page(paginator.num_pages)
    return render_to_response('awaaz/isu.html', {'issues':issues}, context_instance=RequestContext(request))


def issue_search(request):	    	
    try:  			
	    p = issue.objects.filter(year=request.POST['issue_year'],month=request.POST['issue_month'])
    except issue.DoesNotExist:    		
	    raise Http404        		
    return render_to_response('awaaz/issue_search.html', {
	    'issue_list': p,})
