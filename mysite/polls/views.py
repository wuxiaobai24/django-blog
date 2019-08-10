from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views import generic

from .models import Question
# Create your views here.


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'lastest_question_list'

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


# def index(request):
#     lastest_question_list = Question.objects.order_by('-pub_date')[:5]

#     context = {
#         'lastest_question_list': lastest_question_list,
#     }
#     return render(request, 'polls/index.html', context)

# def detail(request, question_id):
#     # return HttpResponse("You're looking at question %s" % question_id)
#     question = get_object_or_404(Question, pk=question_id)
#     context = {
#         'question': question,
#     }
#     return render(request, 'polls/detail.html', context)

# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     context = {'question': question}
#     return render(request, 'polls/results.html', context=context)


def vote(request, question_id):
    # return HttpResponse("You're voting on question %s" % question_id)
    question = get_object_or_404(Question, pk=question_id)
    try:
        selectd_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        context = {
            'question': question,
            'error_message': 'You didn\'t select a choice'
        }
        return render(request, 'polls/details.html', context=context)
    else:
        selectd_choice.votes += 1
        selectd_choice.save()
        return HttpResponseRedirect(
            reverse('polls:results', args=(question_id, )))
