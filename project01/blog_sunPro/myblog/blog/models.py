from django.db import models

# Create your models here.
class BlogPost(models.Model):
    title= models.CharField(max_length=100)
    content = models.TextField

    def _str_(self):
        return self.title