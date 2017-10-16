from django.contrib import admin

# Register your models here.

from .models import user
admin.site.register(user)

from .models import student
admin.site.register(student)

from .models import event
admin.site.register(event)

from .models import grade
admin.site.register(grade)

from .models import activitie
admin.site.register(activitie)

from .models import note
admin.site.register(note)
