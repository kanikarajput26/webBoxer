from django.http import HttpResponse
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, render_to_response
from django.shortcuts import redirect
from django.views import generic
# from datetime import datetime
from django.http import Http404
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import messages
from django.core.urlresolvers import reverse
import simplejson
from . import models
import datetime
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
from django import forms
from django_countries.widgets import CountrySelectWidget
from content.models import Content
from django.contrib.auth.mixins import LoginRequiredMixin
import pymongo


client = pymongo.MongoClient()
db = client.webBoxer

class ContentList(LoginRequiredMixin,ListView):
    model = Content

class ContentCreate(CreateView):
    model = Content
    fields = ['name','url','iconfile','position','mobiletype','partner','country']
    widgets = {'country': CountrySelectWidget()}
    success_url = reverse_lazy('content:content_list')

class ContentUpdate(UpdateView):
    model = Content
    fields = ['name','url','iconfile','position','mobiletype','partner','country']
    success_url = reverse_lazy('content:content_list')

class ContentDelete(DeleteView):
    model = Content
    success_url = reverse_lazy('contact:content_list')


def getFeatureData(partner,screenSize=None):
    templatename='badfeature.html'
    icons = Content.objects.all().filter(mobiletype='others',partner=partner)
    mydict = {}
    i = 1
    for icon in icons:
        if i <=8:
            mykey = "key"+str(i)
            mydict[mykey] = {'name':icon.name,
                              'url':icon.url,
                              'iconurl':icon.iconfile.url
                              }
            i = i+1
        else:
            break
    return {'data':mydict,'os':None,'partner':partner}, templatename


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def MainView(request,partner):
    partner = partner
    try:
        browser = request.user_agent.browser.family
        os = request.user_agent.os.family
    except Exception, e:
        browser = None
        os = None
    print os,browser
    device = request.user_agent.device.family
    ip = get_client_ip(request)
    db.clicks.insert({"partner":partner,"ip":ip,"browser":browser,"os":os,"device":device})
    modernBrowserList = ['mobile safari', 'chrome', 'chromium','opera', 'opera mini','firefox']
    # if browser:
    #     if browser.lower() in modernBrowserList:
    #         if os =='Android':
    #             templatename = 'mainAndroid.html'
    #         elif os =='iOS':
    #             templatename = 'mainios.html'
    #         elif os =='Windows':
    #             templatename = 'mainwin.html'
    #         else:
    #             templatename = 'mainfeature.html'
    #         return render_to_response(templatename)
    #     else:
    if os:
        if os =='Android':
            templatename = 'mainAndroid.html'
        elif os=='iOS':
            templatename='mainios.html'
        elif os=='Windows':
            templatename = 'mainwin.html'
        else:
            if browser.lower()=='other':
                mydict,templatename = getFeatureData(partner)
                return render_to_response(templatename,mydict)
            else:
                templatename = 'mainfeature.html'
        return render_to_response(templatename,{'os':os,'partner':partner})
    else:
        templatename = 'mainfeature.html'
        return render_to_response(templatename,{'os':os,'partner':partner})
            


def ContentFeeder(request):
    partner = request.GET['partner']
    mobiletype = request.GET['mobiletype']
    icons = Content.objects.all().filter(mobiletype=mobiletype,partner=partner)
    mylist =[]
    for icon in icons:
        mylist.append({'name':icon.name,'url':icon.url,'iconfile':icon.iconfile.url})
    return HttpResponse(simplejson.dumps(mylist),content_type="application/json")
