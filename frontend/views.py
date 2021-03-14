from django.shortcuts import render

# Create your views here.
def some_view(request):
    return render(request, 'frontend/main.html')