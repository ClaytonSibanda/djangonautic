from django import forms
from . import models
#creating a model forms

class CreateArticle(forms.ModelForm):
    class Meta:
        model=models.Article
        fields=['title','body','slug','thumb']
