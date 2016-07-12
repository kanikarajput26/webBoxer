from django.conf.urls import url
from . import views

urlpatterns =[
    url(r'count/',views.Count,name="count"),
]