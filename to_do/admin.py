from django.contrib import admin
from .models import ToDoListModel,CustomerUser

# Register your models here.
admin.site.register(CustomerUser)
admin.site.register(ToDoListModel)