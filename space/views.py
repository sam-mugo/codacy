from django.db.models import Q
from django.shortcuts import get_object_or_404, render
from .models import Tutorial, Category

# Create your views here.


def index(request):
    tuts = Tutorial.objects.all()
    return render(request, 'space/index.html', {'tuts': tuts})


def code(request):
    tuts = Tutorial.objects.all()
    return render(request, 'space/code.html', {'tuts': tuts})


# def search(request):
#     query = request.GET.get('query', '')
    
#     posts = Tutorial.objects.filter(status=Tutorial.ACTIVE).filter(Q(title__icontains=query) | Q(intro__icontains=query) | Q(body__icontains=query))
    
#     return render(request, 'blog/search.html', {'posts': posts, 'query': query})