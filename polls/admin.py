from django.contrib import admin
from .models import Question
from .models import Choice
# Register your models here.


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    # The first element of each tuple in fieldsets is the title of the fieldset.
    # fieldsets = [
    #     (None,               {'fields': ['question_text']}),
    #     ('Date information', {'fields': ['pub_date']}),
    # ]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    inlines = [ChoiceInline]
    search_fields = ['question_text']


admin.site.register(Question, QuestionAdmin)
