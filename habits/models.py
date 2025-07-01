from django.db import models
from django.contrib.auth.models import User 

# Create your models here.

class DailyHabit(models.Model):
    user = models.ForeignKey(User , on_delete=models.SET_NULL, null=True , blank= True)
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    date_added = models.DateField()
    updated_date = models.DateField(auto_now=True)
    is_daily = models.BooleanField()
    is_completed = models.BooleanField()
    
    def __str__(self):
        return f'{self.user.username} - {self.name}' 