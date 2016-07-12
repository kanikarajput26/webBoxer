from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from pymongo import MongoClient
import utils
import datetime

client = MongoClient()
db = client.webBoxer
collect = db.clicks


def Count(request):
    time_from = datetime.time(0, 0, 0)


    ## today's count
    d1 = datetime.date.today()
    start1 = datetime.datetime.combine(d1,time_from).isoformat()
    end1 = datetime.datetime.now().isoformat()
    count1 = utils.Processor1(collect,start1,end1)

    ## yesterday's count
    d2 = d1 - datetime.timedelta(days=1)
    t2_upto =datetime.time(23,59,59)
    start2 = datetime.datetime.combine(d2,time_from).isoformat()
    end2 = datetime.datetime.combine(d2,t2_upto).isoformat()
    count2 = utils.Processor1(collect,start2,end2)

    ## whole month's count
    days = d1.day
    d3 = d1 - datetime.timedelta(days=days-1)
    start3 = datetime.datetime.combine(d3,time_from).isoformat()
    count3 = utils.Processor1(collect,start3,end1)

    ## whole year's count
    start = datetime.datetime.combine(d1, time_from)
    year = start.year
    d4 = datetime.date(year,1,1)
    start4 = datetime.datetime.combine(d4,time_from).isoformat()
    count4 = utils.Processor1(collect,start4,end1)

    templatename = 'Order_view.html'
    return render_to_response(templatename,{'count1':count1,'count2':count2,'count3':count3,'count4':count4})









