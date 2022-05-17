from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

# Create your models here.
class Section(models.Model):
    name = models.CharField(max_length=96)
    description = models.TextField()

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=128)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        default=None
    )
    created_on = models.DateTimeField(auto_now_add=True)
    body = models.TextField()

    section = models.ForeignKey(
        Section,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        default=None
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article_detail', args=[self.id])