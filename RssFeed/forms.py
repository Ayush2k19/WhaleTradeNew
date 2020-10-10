from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields={'title','author','body','img_field'}
        widgets={
           'title': forms.TextInput(attrs={'class': 'form-control'}),

           #'author': forms.Select(attrs={'class': 'form-control'}),
           'author': forms.TextInput(attrs={'class': 'form-control','value':'','id':'elder','type':'hidden'}),
           'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Your text here!'}),
        }

class EditForm(forms.ModelForm):
    class Meta:
        model=Post
        fields={'title','body'}
        widgets={
           'title': forms.TextInput(attrs={'class': 'form-control'}),
           #'author': forms.Select(attrs={'class': 'form-control'}),
           'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Edit your text here!'}),
        }
