from django.db import models
from django.urls import reverse
from django.utils import timezone
import datetime


# Create your models here
class Post(models.Model):
    title = models.CharField(max_length=255,help_text="Enter a title")
    slug = models.SlugField(max_length=255,unique=True)
    summary = models.CharField(max_length = 300)
    content = models.TextField()
    published = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created']
        
        def __unicode__(self):
            return u'%s'%self.title
    def get_absolute_url(self):
            return reverse('smallthings.views.post',args=[self.slug])
        
class NewPost(models.Model):
    title = models.CharField(max_length=255,help_text="Enter a title")
    slug = models.SlugField(max_length=255,unique=True)
    
    Study = 'Study'
    Technology = 'Technology'
    Lifestyle = 'Lifestyle'
    Sports = 'Sports'
    News = 'News'
    Gaming = 'Gaming'
    Other = 'Other'
    
    categories = (
            (Study,'Study'),
            (Technology,'Technology'),
            (Lifestyle,'Lifestyle'),
            (Sports,'Sports'),
            (News,'News'),
            (Gaming,'Gaming'),
            (Other,'Other'),
            )
    cat = models.CharField(max_length=20,choices=categories, default= Technology, help_text="Enter a category")
    keywords = models.CharField(max_length=40,help_text="Enter a keywords")
    author = models.CharField(max_length=30,help_text="Enter author name")
    
    images = 'images'
    thumbs = 'thumbs'
    image = models.ImageField(upload_to=images, default ='images/def.jpg')
    thumb = models.ImageField(upload_to=images, default ='thumbs/def.jpg')
    
    
    
    summary = models.CharField(max_length = 300)
    content = models.TextField()
    published = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created']
        
        def __unicode__(self):
            return u'%s'%self.title
    def get_absolute_url(self):
            return reverse('smallthings.views.post',args=[self.slug])
    def __str__(self):
        return ' {} by {} '.format(self.title, self.author)
        
class Comments(models.Model):
    post = models.ForeignKey(NewPost, related_name='comments',on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created',)
        

    def __str__(self):
        return 'Comment by {} on Post - {}'.format(self.name, self.post)

