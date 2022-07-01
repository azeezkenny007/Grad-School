from django.db import models

# Create your models here.


class Information(models.Model):
    title = models.CharField(max_length=2000)
    description1 = models.TextField()
    description2 = models.TextField()
    info=models.CharField(max_length=2000,null=True)
    icon=models.CharField(max_length=2000,null=True)
    
    def __str__(self):
     return f'{self.title}'
