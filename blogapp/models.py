from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length = 20, null = False)
    content = models.TextField(max_length = 300, null = False)
    date = models.DateTimeField('date published')


class Photo(models.Model):
    title = models.CharField(max_length = 20)
    image = models.ImageField(upload_to='images/')
    des = models.CharField(max_length = 500)

    def __str__(self):
        return self.title

    