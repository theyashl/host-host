from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=200)
    manifest = models.TextField()
    poster = models.URLField()

    def publish(self):
        self.save()

    def __str__(self):
        return self.title