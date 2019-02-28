from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls import include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from articles import views as article_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/',  views.about),
    path('home/', views.home),
    path('articles/',include('articles.urls')),
    path('accounts/',include('accounts.urls')),
    path('',article_views.article_list,name="home"),
]

urlpatterns+=staticfiles_urlpatterns()#checks first if we are in debug mode
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
