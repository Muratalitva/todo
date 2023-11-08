from django.shortcuts import render
from Todo.models import Todo
# Create your views here.
def index(request):
    todo = Todo.objects.all()

    return render(request, 'index.html', locals())