from __future__ import unicode_literals
from django.db import models
from mongoengine import *


class Ordered_list(Document):
    count_today = StringField()
    count_yesterday = StringField()
    count_month = StringField()
    count_year = StringField()


