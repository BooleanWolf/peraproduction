from django.contrib import admin
from .models import announcements, assignments, class_tests, helpwewant, routineTasks

admin.site.site_header = 'Mechanical 20 Dashboard'


admin.site.register(announcements)
admin.site.register(assignments)
admin.site.register(class_tests)
admin.site.register(helpwewant)
admin.site.register(routineTasks)
# admin.site.register(Demo)


# Register your models here.
