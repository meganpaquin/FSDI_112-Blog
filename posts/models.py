from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=45)
    body = models.TextField()
    category = models.CharField(max_length=45)
    created_on = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', args=[self.id])
