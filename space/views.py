from django.shortcuts import get_object_or_404, render
from .models import Tutorial, Category

# Create your views here.

def index(request):
    return render(request, 'space/index.html')

def bul(request):
    tuts = Tutorial.objects.all()
    return render(request, 'space/bul.html', {'tuts': tuts})

