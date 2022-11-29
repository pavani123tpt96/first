from django.shortcuts import render

# Create your views here.
def a1_first(request):
    d={'a':200}
    return render(request,'a1_first.html',d)