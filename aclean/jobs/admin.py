from django.contrib import admin
from .models import Job, Task, SiteVisit, Expense, LineItem, JobNote

# Register your models here.
admin.site.register(Job)
admin.site.register(Task)
admin.site.register(SiteVisit)
admin.site.register(Expense)
admin.site.register(LineItem)
admin.site.register(JobNote)