from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import ToDoListModel,CustomerUser
from .forms import ToDoForm

# Register your models here.
class CustomUserAdmin(UserAdmin):
    model = CustomerUser
    list_display = ("username", "is_staff", "is_active",)
    list_filter = ("username", "is_staff", "is_active",)
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "groups", "user_permissions")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "username", "password1", "password2", "is_staff","is_active", "groups", "user_permissions","roles"
            )}
        ),
    )
    search_fields = ("username",)
    ordering = ("username",)



class ToDoAdmin(admin.ModelAdmin):
    form = ToDoForm
    list_display = ('task','status','user')
    search_fields = ('task',)


admin.site.register(CustomerUser, CustomUserAdmin)
admin.site.register(ToDoListModel,ToDoAdmin)