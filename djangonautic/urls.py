from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/',  views.about),
    path('home/', views.home),
    path('articles/',include('articles.urls')),
    path('',views.home),
]
