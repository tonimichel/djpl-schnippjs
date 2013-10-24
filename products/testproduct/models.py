from django.db import models



class News(models.Model):
    name = models.CharField(max_length=111)
    teaser = models.TextField(verbose_name='Teasertext', help_text='This is some help_text')
    category = models.ForeignKey('Category', null=True, blank=True)
    rating = models.IntegerField()
    somefloat = models.FloatField(default=0.11)


class Category(models.Model):
    name = models.CharField(max_length=111)
    
    
    
    
    
    
    
