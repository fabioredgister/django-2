from django.db import models

# Create your models here.

from django.conf import settings
from django.utils import timezone
# from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# class Categoria(models.Model):
#     nome = models.CharField(max_length=50)
#     def __str__(self):
#         return self.nome

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    # text = models.TextField()
    text = RichTextUploadingField()
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    imagens_de = models.CharField(max_length=50)
    # categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def published(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title