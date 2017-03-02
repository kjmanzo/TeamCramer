from django.shortcuts import render
from django.template import loader

# Create your views here.
from django.http import HttpResponse
from .models import Charity

# Shows list of charities in DB
def index(request):
    latest_charity_list = Charity.objects.order_by('-name')[:5]
    context = {'latest_charity_list': latest_charity_list}
    return render(request, 'rewards_app/index.html', context)
