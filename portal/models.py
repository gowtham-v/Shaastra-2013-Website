# Create your models here.
from django.db import models
from django.contrib import admin
from django.utils.safestring import mark_safe

#Allows for updating status of event
STATUS_CHOICES = (
    ('s', 'Sold'),
    ('a', 'Available'),
)
#To specify kind of sponsor
SPONSOR_CHOICES = (
    ('Principal Sponsor', 'Principal Sponsor'),
    ('Associate Sponsor', 'Associate Sponsor'),
    ('Co Sponsor', 'Co Sponsor'),
    ('Event Sponsor', 'Event Sponsor'),
    ('Hospitality Sponsor', 'Hospitality Sponsor'),
    ('Outreach Sponsor', 'Outreach Sponsor'),
    ('Associate Sponsor', 'Associate Sponsor'),
    ('Apparel Sponsor', 'Apparel Sponsor'),
    ('Gift Sponsor', 'Gift Sponsor'),
    ('Research Partner', 'Research Partner'),
    ('Green Partner', 'Green Partner'),
    ('Data Partner', 'Data Partner'),
    
)

class Category(models.Model):
	"""
	This model is for storing the name and generating the url name of the various categories 
	under which events fall.
	"""
	name = models.CharField(max_length=30, unique=True)
	url_name = models.CharField(max_length=30, blank=True)
    
	class Meta:
		verbose_name_plural = "categories"
    	
	def get_events(self):
		return self.events.all()
	get_events.short_description = 'Events'
    
	def __unicode__(self):
		return self.name
    
class Event(models.Model):
	"""
	This model is for storing the information about the events
	"""
	category = models.ForeignKey(Category, related_name = 'events')
	title = models.CharField(max_length=30, unique=True)
	about = models.TextField(blank=True)
	status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='a')
 
	def __unicode__(self):
		return self.title
"""
Image classes to add any number of images for a category/event
"""
        
class CategoryImage(models.Model):
    name=models.CharField(max_length=30, blank=True)
    image=models.ImageField(upload_to='category',null=True,blank=True)
    category=models.ForeignKey(Category, related_name = 'categoryimages')
    def __unicode__(self):
        return self.name

class EventImage(models.Model):
    name=models.CharField(max_length=30, blank=True)
    image=models.ImageField(upload_to='event',null=True,blank=True)
    event=models.ForeignKey(Event, related_name = 'eventimages')
    def __unicode__(self):
        return self.name

class Topic(models.Model):
    """
    This model is for the various topics in the index apart from events, info under them
    """
    title=models.CharField(max_length=500, help_text='As to be displayed in navigation bar on the website')
    url_name=models.CharField(max_length=500)
    information=models.TextField(blank=True)
    #index_number provides the information about the order in which we need to display the topics
    index_number=models.IntegerField(help_text='Determines the order in which topic is displayed in the navigation bar')
    def __unicode__(self):
        return self.title

    def display_mySafeField(self):
        return mark_safe(self.information)
    
    class Meta:
        ordering=['index_number']

class TopicImage(models.Model):
	"""
	a separate model for images related to topics enable us to have
	any number of images being associated with a each topic
	"""
	name=models.CharField(max_length=75,blank=True)
	image=models.FileField(upload_to='topic',null=True,blank=True)
	topic=models.ForeignKey(Topic,related_name='topicimage')
	def __unicode__(self):
		return self.name
	

class PreviousSponsor(models.Model):
    """
    This model is for adding details about 2011 sponsors
    """
    logo=models.ImageField(upload_to='sponsors',null=True,blank=True)
    name=models.CharField(max_length=20,unique=True, help_text='Enter company name (Required)')
    url=models.URLField(blank=True)
    about=models.CharField(max_length=100, choices=SPONSOR_CHOICES, blank=True)
    def __unicode__(self):
		return self.name