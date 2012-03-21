from django.shortcuts import render_to_response,get_object_or_404
from django.template import RequestContext

def about(request):
    context = RequestContext(request)
    return render_to_response('awaaz/abt.html',context_instance = context)

def contact(request):
    context = RequestContext(request)
    return render_to_response('awaaz/cnt.html',context_instance = context)

def sponsors(request):
    context = RequestContext(request)
    return render_to_response('awaaz/sponsors.html',context_instance = context)

def about_gym(request):
    context = RequestContext(request)
    return render_to_response('awaaz/aboutgym.html',context_instance = context)

def postbearers(request):
    context = RequestContext(request)
    return render_to_response('awaaz/postbearers.html',context_instance = context)

def gym_cal(request):
    context = RequestContext(request)
    return render_to_response('awaaz/gymcal.html',context_instance = context)

