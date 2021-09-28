from rest_framework import serializers
from .models import Survey, Question, ChoiceAnswer, Answer


class SurveySerializer(serializers.ModelSerializer):

    class Meta:
        model = Survey
        fields = ['id', 'name_survey', 'description', 'start_date', 'end_date']


class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = ['id', 'question_text', 'poll']


class ChoiceAnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = ChoiceAnswer
        fields = ['id', 'answer_name', 'choices']


class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = ['id', 'author', 'one_choice']