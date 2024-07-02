from django.shortcuts import get_object_or_404, render
from .models import ChaiVariety

def all_chai(request):
  chais = ChaiVariety.objects.all()
  return render(request, 'all_chai.html', {'chais': chais})

def chai_detail(request, chai_id):
  chai = get_object_or_404(ChaiVariety, pk=chai_id)
  return render(request, 'chai_detail.html', {'chai': chai, 'hide_navbar': True})

def create_order(request, chai_id):
  return render(request, 'under_construction.html', {'hide_navbar': True})