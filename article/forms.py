from django import forms

from .models import Article

class AddartilceForm(forms.ModelForm):
    class Meta():
        model=Article
        fields=["title","content","article_image"]