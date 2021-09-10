from django.db import models

# Create your models here.


class Student(models.Model):
    name  = models.CharField(max_length=255, null=False, blank=False)
    age   = models.IntegerField(null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    active 	  = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated   = models.DateTimeField(auto_now_add=False, auto_now=True)
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-timestamp',)