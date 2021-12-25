from django.shortcuts import render
from .models import event
# Create your views here.
def index(request):
    nt= event.objects.all()
    data={'dat':nt}
    return render(request,"index.html",data)