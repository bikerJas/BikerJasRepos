from django.http import HttpResponse
from django.shortcuts import render
import sys
from subprocess import run, PIPE


def button(request):
    return render(request, 'my_template.html')


def external(request):
    out = run([sys.executable, 'D://Documents//PythonProjects//Coursera//Lotto.py'], shell=False, stdout=PIPE)
    print(out)
    return HttpResponse(out.stdout)
