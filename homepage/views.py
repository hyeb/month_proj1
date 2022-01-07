from django.shortcuts import render

# Create your views here.

def airplane(request):
    return render(request, 'airplane_edit.html', {})