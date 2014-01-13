# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext, Template


def hometasks(request):
	return render_to_response('basic.html', context_instance=RequestContext(request))
