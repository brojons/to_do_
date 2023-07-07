from django.db import models
import datetime

# Create your models here.
class ToDoListModel(models.Model):
    task = models.CharField(max_length=250)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=datetime.datetime.now)
    update_at = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return self.task

    class Meta:
        db_table = 'to_do_list'