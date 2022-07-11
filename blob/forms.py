from unicodedata import category
from django import forms
from .models import Post, Category

choices = Category.objects.all().values_list("name", 'name')


class CategoryForm (forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name',)

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }


class PostForm (forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "author", "category", "body")

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'title'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=choices, attrs={'class': 'form-control'}),
            'body': forms.TextInput(attrs={'class': 'form-control'}),
        }


class EditForm (forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "body", "category")

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=choices, attrs={'class': 'form-control'}),
            'body': forms.TextInput(attrs={'class': 'form-control'}),
        }
