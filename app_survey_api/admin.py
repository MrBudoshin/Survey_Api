from django.contrib import admin
from .models import Survey, Question, ChoiceAnswer


class SurveyAdmin(admin.ModelAdmin):
    models = Survey
    list_display = ['name_survey', 'description', 'start_date', 'end_date']


class QuestionAdmin(admin.ModelAdmin):
    models = Question
    list_display = ['question_text']


class ChoiceAnswerAdmin(admin.ModelAdmin):
    models = ChoiceAnswer
    list_display = ['answer_name']


admin.site.register(Survey, SurveyAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(ChoiceAnswer, ChoiceAnswerAdmin)

