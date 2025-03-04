from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Actor(BaseModel):
    name = models.CharField(max_length=100)
    birthdate = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name


class Movie (models.Model):
    name = models.CharField(max_length=100)
    year = models.IntegerField()
    imdb_id = models.ImageField(upload_to='movies', null=True, blank=True)
    genre = models.CharField(max_length=100)
    actors = models.ManyToManyField(Actor)

    def __str__(self):
        return self.name


