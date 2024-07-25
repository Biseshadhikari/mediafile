from django.db import models

# Create your models here.


class Todolist(models.Model): 
    title = models.CharField(max_length=200)
    is_completed = models.BooleanField()
    img = models.ImageField(null=True,blank=True,upload_to='img')
    
    
    
    def __str__(self):
        return f"{self.title}-{self.is_completed}"