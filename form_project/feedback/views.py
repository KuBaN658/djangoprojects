from django.shortcuts import render
from django.http import HttpResponseRedirect

def index(request):
    if request.method == 'POST':
        name = request.POST['name']
        if len(name) == 0:
            return render(request, 'feedback/feedback.html', context={'got_error': True})
        print(name)
        return HttpResponseRedirect('/done')
    return render(request, 'feedback/feedback.html', context={'got_error': False})


def done(request):
    return render(request, 'feedback/done.html')
