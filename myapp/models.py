from django.db import models
# Create your models here.
class Post(models.Model):
    title = models.CharField(
        max_length=50,
        blank=True,
        null=True,
    )
    description = models.CharField(max_length=50)
    created_date =  models.DateTimeField()
    attachment = models.FileField(
        upload_to="media/",
        blank=True,
        null=True,
    )