from django.contrib import admin

from assesments.models import Assesment, Instance, Taker, Question, Option

admin.site.register(Assesment)
admin.site.register(Instance)
admin.site.register(Taker)
admin.site.register(Question)
admin.site.register(Option)
