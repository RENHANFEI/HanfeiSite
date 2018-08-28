from django.shortcuts import render
from django.http import StreamingHttpResponse
from . import settings

def page_not_found(request):
    context = {}
    context['title'] = '404 Page Not Found'
    context['styles'] = ['error.css']
    context['nav'] = 'error'
    return render(request, '404.html', context)

def page_error(request):
    context = {}
    context['title'] = '500 Error'
    context['styles'] = ['error.css']
    context['nav'] = 'error'
    return render(request, '500.html', context)

def work(request):
    context = {}
    context['title'] = 'Hanfei REN'
    context['nav'] = 'work'
    context['styles'] = ['work.css']
    return render(request, 'work.html', context)

def standup(request):
    context = {}
    context['title'] = 'StandUp | Hanfei REN'
    context['nav'] = 'project'
    context['styles'] = ['standup.css']
    return render(request, 'standup.html', context)

def cubicle(request):
    context = {}
    context['title'] = 'Cubicle | Hanfei REN'
    context['nav'] = 'project'
    context['styles'] = ['cubicle.css']
    return render(request, 'cubicle.html', context)

def casio(request):
    context = {}
    context['title'] = 'Casio IUR | Hanfei REN'
    context['nav'] = 'project'
    context['styles'] = ['casio.css']
    return render(request, 'casio.html', context)

def stepbeats(request):
    context = {}
    context['title'] = 'StepBeats | Hanfei REN'
    context['nav'] = 'project'
    context['styles'] = ['stepbeats.css']
    return render(request, 'stepbeats.html', context)

def kiwi(request):
    context = {}
    context['title'] = 'Kiwi | Hanfei REN'
    context['nav'] = 'project'
    context['styles'] = ['kiwi.css']
    return render(request, 'kiwi.html', context)

def projects(request):
    context = {}
    context['title'] = 'Projects | Hanfei REN'
    context['nav'] = 'project'
    context['styles'] = ['projects.css']
    return render(request, 'projects.html', context)

def about(request):
    context = {}
    context['title'] = 'About | Hanfei REN'
    context['nav'] = 'about'
    context['styles'] = ['about.css']
    return render(request, 'about.html', context)


def resume(request):

    def file_iterator(file_name, chunk_size=512):
        with open(file_name) as f:
            while True:
                c = f.read(chunk_size)
                if c:
                    yield c
                else:
                    break

    the_file_name = settings.STATIC_URL + "resume.pdf"
    response = StreamingHttpResponse(file_iterator(the_file_name))
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="{0}"'.format(the_file_name)

    return response
