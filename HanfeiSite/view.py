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

import os
from time import time
from random import randint
from vcd_settings import *  # get vcd_pairs and vcd_dir

# for vision correcting displays (MEng capstone)
def vcd(request):
    
    context = {}
    context['title'] = 'VCD Image Quality Assessment'
    context['styles'] = ['vcd.css']
    context['nav'] = 'error'
    now_time = time()
    context['submit'] = True

    # have group_id, check if is the last image
    if "group_id" in request.COOKIES and "pair_id" in request.COOKIES and "start_time" in request.COOKIES:

        group_id = int(request.COOKIES['group_id'])
        pair_id = int(request.COOKIES['pair_id'])
        start_time = float(request.COOKIES['start_time'])

        group = vcd_pairs[group_id]

        # if post, get rating
        if request.POST:
            # check validity
            now_time = time()
            period = now_time - start_time
            if pair_id < pair_num and pair_id >= 3: # first three for adaptation
            
                # get pair and store it
                rating = request.POST['rating']
                # store it
                # context['record'] = sys.path[0] + record_path
                module_dir = os.path.dirname(__file__)  # get current directory
                file_path = os.path.join(module_dir, record_path)
                with open(file_path, 'a+') as f:
                    im1, im2 = group[pair_id]
                    im, param1 = im1.split('.')[0].split('_')
                    param2 = im2.split('.')[0].split('_')[1]
                    model1 = param1[:-1]
                    size1 = param1[-1]
                    model2 = param2[:-1]
                    size2 = param2[-1]
                    record = ','.join([im, model1, size1, model2, size2, rating, 
                        str(period), str(now_time)]) + '\n'
                    f.write(record)

            if pair_id < pair_num:
                pair_id += 1

        if pair_id < pair_num:
            pair = group[pair_id]

        else:
            pair = group[pair_id - 1]
            context['submit'] = False

    # if no group_id, generate one and initialize pair_id to 0
    else:
        group_id = randint(0, group_num)
        pair_id = 0
        pair = vcd_pairs[group_id][pair_id]

    # show images
    im1, im2 = pair
    context['im1'] = os.path.join(vcd_dir, im1)
    context['im2'] = os.path.join(vcd_dir, im2)
    context['group_id'] = group_id
    context['pair_id'] = pair_id
    context['pair_num'] = pair_num
    context['process'] = int(pair_id * 1000 / pair_num) / 10.
    
    response = render(request, 'vcd.html', context)
    response.set_cookie("pair_id", pair_id)
    response.set_cookie("group_id", group_id)
    response.set_cookie("start_time", now_time)
    return response


