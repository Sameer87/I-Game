from django.contrib import admin
from .models import Question,Submission,connection
# Register your models here.
admin.site.register(Question)
admin.site.register(Submission)
admin.site.register(connection)