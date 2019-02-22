from django.db import models

# Create your models here.
class Article(models.Model):
    '''  This is the definition of the article model '''
    title = models.CharField(max_length=100)
    slug =  models.SlugField(max_length=100)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    #add thumbnail later
    #add author later

    def __str__(self):
        ''' gives a string representation of the article '''
        return self.title

    def snippet(self):
        ''' gives a shortened version of the  article detail'''
        return self.body[:50]+'...'
