from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomerUser(AbstractUser):
    ROLE_CHOICES = (
        ('a','admin'),
        ('u','user')
    )

    roles = models.CharField(max_length=1,choices=ROLE_CHOICES)

class ToDoListModel(models.Model):
    task = models.CharField(max_length=250)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=datetime.now)
    update_at = models.DateTimeField(default=datetime.now)
    user = models.ForeignKey(CustomerUser,on_delete=models.CASCADE,default=None,null=True)

    def __str__(self):
        return self.task

    class Meta:
        db_table = 'to_do_list'