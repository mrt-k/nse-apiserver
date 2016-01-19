#from django.shortcuts import render
import django_filters
from rest_framework import viewsets, filters
from rest_framework import generics

from api.models import Nse, NseArgv
from api.serializer import NseSerializer, NseArgvSerializer

class CategoryFilterBackend(filters.BaseFilterBackend):
    """
    Filter that only allows users to see their own objects.
    """
    def filter_queryset(self, request, queryset, view):
        queryset = Nse.objects.all()
        category = request.query_params.get('category', None)
        if category is not None:
             queryset = queryset.filter(category__contains=category)
        return queryset


class NseArgvViewSet(viewsets.ModelViewSet):
    queryset = NseArgv.objects.all()
    serializer_class = NseArgvSerializer


class NseViewSet(viewsets.ModelViewSet):
    queryset = Nse.objects.all()
    serializer_class = NseSerializer
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter, CategoryFilterBackend)
    filter_fields = ('name', 'category', 'author')
    search_fields = ('name', 'category', 'author')
