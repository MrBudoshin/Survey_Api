from django.contrib.auth.models import User

from django.db import models


class Survey(models.Model):
    """Опрос"""
    name_survey = models.CharField(max_length=200, db_index=True, verbose_name="Опрос")
    description = models.TextField(verbose_name="Описание")
    start_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата начала опроса")
    end_date = models.DateTimeField(verbose_name="Дата конца опроса")

    def __str__(self):
        return f'{self.name_survey}, {self.description}, {self.start_date}, {self.end_date}'

    class Meta:
        verbose_name = 'Опрос'
        verbose_name_plural = 'Опросы'


class Question(models.Model):
    """Вопрос"""
    question_text = models.TextField()
    poll = models.ForeignKey('Survey', db_index=True, blank=True, on_delete=models.CASCADE, related_name="poll")

    def __str__(self):
        return f'{self.question_text}'

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


class ChoiceAnswer(models.Model):
    """Варианты ответа"""
    answer_name = models.TextField(verbose_name='Вариант ответа')
    choices = models.ForeignKey('Question', on_delete=models.CASCADE, related_name="choices")

    def __str__(self):
        return f'{self.answer_name}'

    class Meta:
        verbose_name = 'Варианты ответа'
        verbose_name_plural = 'Варианта ответов'


class Answer(models.Model):
    """Вариант ответа на вопрос"""
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    one_choice = models.ForeignKey('ChoiceAnswer', null=True, on_delete=models.CASCADE,
                                   related_name="answers_one_choice")

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'
