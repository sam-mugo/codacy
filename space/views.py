from django.db.models import Q
from django.shortcuts import get_object_or_404, render
from rest_framework.generics import ListAPIView
from .models import Tutorial
from .serializers import TutorialSerializer
from taggit.models import Tag

# Create your views here.


def index(request):
    all_tuts = Tutorial.objects.all()
    return render(request, 'space/index.html', {'all_tuts': all_tuts})


def tuts(request):
    tuts = Tutorial.objects.all()
    tags = Tag.objects.all()
    context = {'tuts': tuts, 'tags': tags}
    return render(request, 'space/tuts.html', context)


class TutorialListAPIView(ListAPIView):
    queryset = Tutorial.objects.all()
    serializer_class = TutorialSerializer



# def search(request):
#     query = request.GET.get('query', '')
    
#     posts = Tutorial.objects.filter(status=Tutorial.ACTIVE).filter(Q(title__icontains=query) | Q(intro__icontains=query) | Q(body__icontains=query))
    
#     return render(request, 'blog/search.html', {'posts': posts, 'query': query})