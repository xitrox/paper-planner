from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PaperSerializer
from .models import Paper

# Create your views here.
from django.http import HttpResponse


class PaperViewSet(viewsets.ModelViewSet):
    queryset = Paper.objects.all().order_by('title')
    serializer_class = PaperSerializer
