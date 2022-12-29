from django.contrib import admin
from .models import Task
#admin.site.register(Task)
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id','title')
    list_filter = ('title',)
    sortable_by = ('title',)

