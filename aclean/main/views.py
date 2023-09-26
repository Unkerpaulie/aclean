from django.shortcuts import render

# Create your views here.
def index(req):
    context = {}
    return render(req, "main/index.html", context)

def login(req):
    pass