from rest_framework import generics, status
from rest_framework.response import Response
from serializers import QuestionSerializer
from models import *
import json
from django.http import Http404
from django.shortcuts import render


class QuestionList(generics.ListAPIView):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()


def index(request):
    questions = Question.objects.order_by('-id')
    context = {'questions': questions}
    return render(request, '../templates/trivia/index.html', context)


def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, '../templates/trivia/detail.html', {'question': question})


class AddQuestion(generics.CreateAPIView):
    serializer_class = QuestionSerializer

    def post(self, request, *args, **kwargs):
        trivia_data = json.loads(request.body)

        question = trivia_data[0]

        question_serializer = QuestionSerializer(data=question)

        if question_serializer.is_valid():
            question_serializer.save()
            return Response(question_serializer.data, status=status.HTTP_201_CREATED)
        print question_serializer.error_messages, question_serializer.errors
        return Response(question_serializer.errors, status=status.HTTP_400_BAD_REQUEST)