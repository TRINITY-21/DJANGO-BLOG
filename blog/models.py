from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post_image = models.ImageField(default = 'default.jpg', upload_to='post_pix') 

    def __str__(self):
        return self.title 

    def get_absolute_url(self):
        return reverse('blog_home')