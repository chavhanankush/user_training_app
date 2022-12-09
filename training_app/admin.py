from django.contrib import admin
from training_app.models import User, Training
# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'email', 'user_role', 'is_staff', 'is_active', 'date_joined']


@admin.register(Training)
class TrainingAdmin(admin.ModelAdmin):
    list_display = ['training_id','training_course','created','updated','description']