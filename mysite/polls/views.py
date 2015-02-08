# -*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone


from polls.models import Choice, Question

class About2View(generic.TemplateView):
    template_name = "about.html"

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.filter(
            pub_date__lte = timezone.now()
        ).order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    p = get_object_or_404(Question, pk= question_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        """如果POST中的choice 不存在会触发KeyError
            如果没有取出内容出发第二个"""
        return render(request, 'polls/detail.html', {
                'question':p,
            'error_message':"you did not select a choice",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))

# def index(request):
#     latest_question_list = \
#         Question.objects.order_by('-pub_date')[:5]
#     context = {'latest_question_list': latest_question_list}
#     return render(request, 'polls/index.html', context)
#
# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/detail.html', {'question':question})
#
# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})
#
#





# def index(request):
#     format_str = "Hello, you are at the polls index"
#     return HttpResponse(format_str)
#
#     latest_question_list = \
#         Question.objects.order_by('-pub_date')[:5]
#
#     template = loader.get_template('polls/index.html')
#     context = RequestContext(
#         request,
#         {
#             'latest_question_list':latest_question_list
#         }
#     )
#     return HttpResponse(template.render(context))

# def detail(request, question_id):
#     format_str = "You're looking at question %s."
#     return HttpResponse(format_str % question_id)
#
#     try:
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404("Question does not have!!!")
#     print '如果404不能看到'
#     return render(request, 'polls/detail.html', {'question':question})

# def results(request, question_id):
#     response = "you are looking at the results of question %s"
#     return HttpResponse(response % question_id)

# def vote(request, question_id):
#     format_str = "u are voting on question %s"
#     return HttpResponse(format_str % question_id)

