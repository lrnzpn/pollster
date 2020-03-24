from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import Http404,  HttpResponseRedirect
from .models import Question, Choice

# Create your views here.


# get questions and display them
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]  # desc
    # pass to template as a dict
    context = {'latest_question_list': latest_question_list}
    # display here and then render questions
    return render(request, 'polls/index.html', context)


# show specific question and choices
def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404('Question does not exist')
    return render(request, 'polls/detail.html', {'question': question})


# get question and display results
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})


# vote for question choice
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # redisplay question voting form
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # return w httpresponseredirect after dealing w post data
        # prevents data from being posted twice when user hits back
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))