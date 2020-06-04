from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse , Http404, HttpResponseRedirect
from django.views import generic
from django.urls import reverse

from .models import Question, Choice

class IndexView(generic.ListView):
    template_name = 'firstapp/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'firstapp/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'firstapp/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        select_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'firstapp/detail.html', {
            'question': question,
            'error_message': "Você não selecionou uma resposta"
        })
    else:
        select_choice.votes +=1
        select_choice.save()
        return HttpResponseRedirect(reverse('firstapp:results', args=(question.id,)))













""" def index(request):
    lastest_questions_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': lastest_questions_list}
    return render(request, 'firstapp/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'firstapp/detail.html', {'question': question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'firstapp/results.html', {'question': question}) """
