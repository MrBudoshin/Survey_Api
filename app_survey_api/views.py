from rest_framework import permissions
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, \
    DestroyModelMixin

from .models import Survey, Question, ChoiceAnswer, Answer
from .serializer import SurveySerializer, QuestionSerializer, ChoiceAnswerSerializer, AnswerSerializer


class SurveyView(ListModelMixin, GenericAPIView):
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer
    permission_classes = (permissions.AllowAny,)

    def get(self, request):
        return self.list(request)


class SurveyDetail(RetrieveModelMixin, GenericAPIView):
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer
    permission_classes = (permissions.AllowAny,)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class QuestionView(ListModelMixin, GenericAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = (permissions.AllowAny,)

    def get(self, request):
        return self.list(request)


class QuestionDetail(RetrieveModelMixin, GenericAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = (permissions.AllowAny,)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class SurveyChoiceAnswerView(ListModelMixin, GenericAPIView):
    queryset = ChoiceAnswer.objects.all()
    serializer_class = ChoiceAnswerSerializer
    permission_classes = (permissions.AllowAny,)

    def get(self, request):
        return self.list(request)


class SurveyChoiceAnswerDetail(RetrieveModelMixin, GenericAPIView):
    queryset = ChoiceAnswer.objects.all()
    serializer_class = ChoiceAnswerSerializer
    permission_classes = (permissions.AllowAny,)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class SurveyAnswerView(ListModelMixin, GenericAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = (permissions.AllowAny,)

    def get(self, request):
        return self.list(request)


class SurveyAnswerDetail(RetrieveModelMixin, GenericAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = (permissions.AllowAny,)

    def get_queryset(self):
        user_id = self.request.user.id
        queryset = Survey.objects.exclude(questions__answers__author__id=user_id)
        return queryset


class SurveyChange(UpdateModelMixin, RetrieveModelMixin, DestroyModelMixin, CreateModelMixin, GenericAPIView):
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer
    permission_classes = (permissions.IsAdminUser,)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def post(self, request):
        return self.create(request)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class QuestionChange(UpdateModelMixin, RetrieveModelMixin, DestroyModelMixin, CreateModelMixin, GenericAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = (permissions.IsAdminUser,)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def post(self, request):
        return self.create(request)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class AnswerChange(UpdateModelMixin, RetrieveModelMixin, DestroyModelMixin, CreateModelMixin, GenericAPIView):
    queryset = ChoiceAnswer.objects.all()
    serializer_class = ChoiceAnswerSerializer
    permission_classes = (permissions.IsAdminUser,)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def post(self, request):
        return self.create(request)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)



