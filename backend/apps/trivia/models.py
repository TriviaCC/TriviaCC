from django.db import models


# class Category(models.Model):
#     title = models.CharField(max_length=100)
#
#     def __str__(self):
#         return self.title


class Question(models.Model):
    question = models.TextField(max_length=5000)
    answer = models.CharField(max_length=50)
    # category = models.ForeignKey(Category, related_name="category", null=True, blank=True)

    def __str__(self):
        return self.question