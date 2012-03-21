from django.shortcuts import render_to_response
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.template import RequestContext
from form.forms import ContactForm

def contact(request):
    errors=[]
    if request.method=='POST':
	    form=ContactForm(request.POST)
	    if form.is_valid():
		    subject=form.cleaned_data['subject']
		    sender=form.cleaned_data['sender']
		    message=form.cleaned_data['message']
		    recipients = ['editor.awaaz@gmail.com']
		    send_mail(subject,message,sender,recipients)
		    return HttpResponseRedirect('/awaaz/contact/thankyou/')
    else:
	    form=ContactForm()
    return render_to_response('awaaz/cnt.html',{
	    'form':form,
	    },context_instance=RequestContext(request))

def thankyou(request):
	return render_to_response('awaaz/thankyou.html')

def gym_contact(request):
    errors=[]
    if request.method=='POST':
	    form=ContactForm(request.POST)
	    if form.is_valid():
		    subject=form.cleaned_data['subject']
		    sender=form.cleaned_data['sender']
		    message=form.cleaned_data['message']
		    recipients = ['mehrotra.pulkit@gmail.com']
		    send_mail(subject,message,sender,recipients)
		    return HttpResponseRedirect('/awaaz/gymkhana/thankyou/')
    else:
	    form=ContactForm()
    return render_to_response('awaaz/gymcontact.html',{
	    'form':form,
	    },context_instance=RequestContext(request))

def gym_thankyou(request):
	return render_to_response('awaaz/gymkhana_thankyou.html')

def your_voice_form(request):
    errors=[]
    if request.method=='POST':
	    form=ContactForm(request.POST)
	    if form.is_valid():
		    subject=form.cleaned_data['subject']
		    sender=form.cleaned_data['sender']
		    message=form.cleaned_data['message']
		    recipients = ['editor.awaaz@gmail.com']
		    send_mail(subject,message,sender,recipients)
		    return HttpResponseRedirect('/awaaz/yourvoice/')
    else:
	    form=ContactForm()
    return render_to_response('awaaz/form.html',{
	    'form':form,
	    },context_instance=RequestContext(request))

def your_voice_thankyou(request):
	return render_to_response('awaaz/yourvoice_thankyou.html')
