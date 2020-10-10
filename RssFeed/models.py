from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date


class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    post_date = models.DateField(auto_now_add=True)
    group_url = models.URLField(max_length=200)
    img_field = models.ImageField(
        upload_to="images/", null=True, blank=True, height_field=None, width_field=None, max_length=100)

    def __str__(self):
        return self.title + '|' + str(self.author)

    def get_absolute_url(self):
        return reverse('article-detail', args=(str(self.id)))
