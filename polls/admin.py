from django.contrib import admin
from . models import *

#to customize django admin area
admin.site.site_header = "Pollapp Admin"
admin.site.site_title = "Pollapp Admin Area"
admin.site.index_title = "Welcome to the Pollapp Admin area"

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['question_text']}),
    ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']}),]
    inlines = [ChoiceInline]    

# Register your models here.
#admin.site.register(Question)
#admin.site.register(Choice)
admin.site.register(Question, QuestionAdmin)
