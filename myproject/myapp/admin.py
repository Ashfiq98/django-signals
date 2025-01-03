from django.contrib import admin
from .models import MyModel, LogEntry
 
admin.site.register(MyModel)
admin.site.register(LogEntry)