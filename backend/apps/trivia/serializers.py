from rest_framework import serializers
from models import Question


# class CategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Category


class QuestionSerializer(serializers.ModelSerializer):
    # category = CategorySerializer(many=False)

    class Meta:
        model = Question

    # def create(self, validated_data):
    #     question = Question.objects.create(**validated_data)
    #     return question