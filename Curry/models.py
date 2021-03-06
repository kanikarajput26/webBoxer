from django.db import models
from django.core.urlresolvers import reverse


class Content(models.Model):
    PositionTypes = (
    	('1','First'),
    	('2','Second'),
    	('3','Third'),
    	('4','Fourth'),
    	('5','Fifth'),
    	('6','Sixth'),
    	('7','Seventh'),
    	('8','Eighth'),
    	('9','Ninth')
    	)
    mobileTypes = (
    	('Android','Android'),
    	('FeaturePhone','other'),
    	('Windows','Windows'),
    	('ios','ios')
    	) 	
    url = models.CharField(max_length=256)
    name = models.CharField(max_length=128)
    iconfile = models.FileField(upload_to='documents/%Y/%m/%d')
    position = models.CharField(max_length=4,choices=PositionTypes)
    partner = models.CharField(max_length=256)
    mobiletype = models.CharField(max_length=128,choices=mobileTypes)
    country = models.CharField(max_length=128)
    
    def __unicode__(self):
    	return self.name

    def get_absolute_url(self):
    	return reverse('intex:content_edit', kwargs={'pk': self.pk})

