from django.shortcuts import render

# Create your views here.
def places(request):
    d={'name':'bangalore'}
    return render(request,'places.html',d)