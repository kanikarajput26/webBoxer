from django.http import HttpResponse
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
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

from Curry.models import Content

class ContentList(ListView):
    model = Content

class ContentCreate(CreateView):
    model = Content
    fields = ['name','url','iconfile','position','mobiletype','partner','country','']
    success_url = reverse_lazy('contact:content_list')

class ContentUpdate(UpdateView):
    model = Content
    fields = ['name', 'pages']
    success_url = reverse_lazy('contact:content_list')

class ContentDelete(DeleteView):
    model = Content
    success_url = reverse_lazy('contact:content_list')