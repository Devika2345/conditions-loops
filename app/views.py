from django.shortcuts import render

# Create your views here.
def conditions(request):
    d={'a':10,'b':20,'c':30}
    return render(request,'conditions.html',d)

def loops(request):
    d={'name':'Devika'}
    return render(request,'loops.html',context=d)
