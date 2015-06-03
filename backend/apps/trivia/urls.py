from django.conf.urls import patterns, url, include
from views import *
from django.contrib import admin


urlpatterns = patterns('',
                       url(r'^trivia/$', index, name='index'),
                       url(r'^trivia/(?P<question_id>[0-9]+)/$', detail, name='detail'),
                       url(r'^admin/', include(admin.site.urls)),
                       # url('^categories/$', CategoryList.as_view(), name='category-list'),
                       # url(r'^categories/(?P<pk>[0-9]+)/$', CategoryDetail.as_view(), name='category-detail'),
                       url('^questions/$', QuestionList.as_view(), name='question-list'),
                       url('^add_question/$', AddQuestion.as_view(), name='add-question'),
                       )