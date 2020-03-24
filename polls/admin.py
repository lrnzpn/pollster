from .models import Question, Choice  # bring in models
from django.contrib import admin

# change site title
admin.site.site_header = 'Pollster Admin'
admin.site.site_title = 'Pollster Admin Area'
admin.site.index_title = 'Welcome to the Pollster Admin Area'


# Register your models here.

# choices withing the questions screen

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['question_text']}),
                 ('Date Information', {'fields': [
                  'pub_date'], 'classes':['collapse']}),
                 ]
    inlines = [ChoiceInline]


# register question, and then the inlined fields
admin.site.register(Question, QuestionAdmin)
# admin.site.register(Question)
# admin.site.register(Choice)
