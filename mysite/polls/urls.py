# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from polls import views


urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<question_id>\d+)/vote/$', views.vote, name='vote'),
    url(r'^about/$', TemplateView.as_view(template_name="about.html")),
    url(r'^about2/$', views.About2View.as_view()),
)

# urlpatterns = patterns('',
#     # ex: /polls/
#     url(r'^$', views.index, name='index'),
#     #url 的名称是用于模板中的
#     # ex: /polls/5/
#     url(r'^(?P<question_id>\d+)/$',     views.detail, name='detail'),
#     # ex: /polls/5/results/
#     url(r'^(?P<question_id>\d+)/results/$', views.results, name='results'),
#     # ex: /polls/5/vote/
#     url(r'^(?P<question_id>\d+)/vote/$', views.vote, name='vote'),
# )
