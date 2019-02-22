from django.contrib import admin
from .models import Article
# Register your models here.

admin.site.register(Article)#tell django to register on the admin side my model
