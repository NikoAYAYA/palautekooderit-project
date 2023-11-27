from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def feedback_index(req):
    return HttpResponse("Hello feedback index")

def feedback_entry(req):
    return HttpResponse("Give feedback here")