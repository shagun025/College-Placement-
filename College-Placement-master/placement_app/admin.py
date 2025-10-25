from django.contrib import admin
from .models import Companies, Interviews, Placements, Students
# Register your models here.

admin.site.register(Companies)
admin.site.register(Interviews)
admin.site.register(Placements)
admin.site.register(Students)