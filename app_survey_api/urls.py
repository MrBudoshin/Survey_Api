from django.urls import path
from .views import SurveyView, SurveyDetail, QuestionView, QuestionDetail, SurveyChoiceAnswerView, \
    SurveyChoiceAnswerDetail, SurveyAnswerView, SurveyAnswerDetail, SurveyChange, QuestionChange, AnswerChange


urlpatterns = [
    path('surveyview/', SurveyView.as_view(), name='surveyview'),
    path('surveydetail/<int:pk>/', SurveyDetail.as_view(), name='surveydetail'),
    path('question', QuestionView.as_view(), name='question'),
    path('questiondetail/<int:pk>/', QuestionDetail.as_view(), name='questiondetail'),
    path('choiceanswer', SurveyChoiceAnswerView.as_view(), name='choiceanswer'),
    path('choiceanswerdetail/<int:pk>/', SurveyChoiceAnswerDetail.as_view(), name='choiceanswerdetail'),
    path('answerview', SurveyAnswerView.as_view(), name='answerview'),
    path('answerdetail/<int:pk>/', SurveyAnswerDetail.as_view(), name='answerdetail'),
    path('change_survey/<int:pk>', SurveyChange.as_view(), name='change_survey'),
    path('change_question/<int:pk>', QuestionChange.as_view(), name='change_question'),
    path('change_choice_answer/<int:pk>', AnswerChange.as_view(), name='change_choice_answer')

]