from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .models import Day
from .serializers import DaySerializer

# Create your views here.


class DayViewSet(viewsets.ModelViewSet):
    queryset = Day.objects.all().order_by('date')
    serializer_class = DaySerializer

def view_index(request):
    return render(request, 'index.html')
