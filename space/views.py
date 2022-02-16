from django.shortcuts import get_object_or_404, render
from .models import Tutorial, Category

# Create your views here.

def index(request):
    return render(request, 'space/index.html')

def index(request):
    tuts = Tutorial.objects.all()
    return render(request, 'space/index.html', {'tuts': tuts})

