from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text', 'image')

# class CategoriaForm(forms.ModelForm):
#     class Meta:
#         model = Categoria
#         fields = ('nome',)