#from django.shortcuts import render
import django_filters
from rest_framework import viewsets, filters
from rest_framework import generics
from api.models import Nse, NseArgv
from api.serializer import NseSerializer, NseArgvSerializer

class CategoryFilterBackend(filters.BaseFilterBackend):
    """
    Categoryのフィルタ
    """
    def filter_queryset(self, request, queryset, view):
        queryset = Nse.objects.all()
        name = request.query_params.get('name', "")
        category = request.query_params.get('category', "")
        author = request.query_params.get('author', "")

        queryset = queryset.filter(name__contains=name) & queryset.filter(category__contains=category) & queryset.filter(author__contains=author)

        return queryset


class NseArgvViewSet(viewsets.ModelViewSet):
    queryset = NseArgv.objects.all()
    serializer_class = NseArgvSerializer
    http_method_names = ['get']



class NseViewSet(viewsets.ModelViewSet):
    queryset = Nse.objects.all()
    serializer_class = NseSerializer
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter, CategoryFilterBackend)
    filter_fields = ('name', 'category', 'author')
    search_fields = ('name', 'category', 'author')
    http_method_names = ['get']
