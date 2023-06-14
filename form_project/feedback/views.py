from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import FeedbackForm

def index(request):

    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/done')
    form = FeedbackForm()
    return render(request, 'feedback/feedback.html', context={'form': form})


def done(request):
    return render(request, 'feedback/done.html')
