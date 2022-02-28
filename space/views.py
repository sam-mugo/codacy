from django.db.models import Q
from django.shortcuts import get_object_or_404, render
from .models import Tutorial, Category

# Create your views here.


def index(request):
    all_tuts = Tutorial.objects.all()
    return render(request, 'space/index.html', {'all_tuts': all_tuts})


def tut(request):
    tuts = Tutorial.objects.all()
    return render(request, 'space/tuts.html', {'tuts': tuts})



# def search(request):
#     query = request.GET.get('query', '')
    
#     posts = Tutorial.objects.filter(status=Tutorial.ACTIVE).filter(Q(title__icontains=query) | Q(intro__icontains=query) | Q(body__icontains=query))
    
#     return render(request, 'blog/search.html', {'posts': posts, 'query': query})