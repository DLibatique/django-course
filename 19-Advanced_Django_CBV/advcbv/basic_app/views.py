from django.shortcuts import render
from django.views.generic import (View, TemplateView,
    ListView, DetailView, CreateView, UpdateView, DeleteView)
# from django.http import HttpResponse
from . import models
from django.urls import reverse_lazy

# Create your views here.

# # function based view
# def index(request):
#     return render(request, 'index.html')

# # class based view
# class CBView(View):
#     def get(self,request):
#         return HttpResponse("Class based views are cool!")

# template view
class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['injectme'] = 'BASIC INJECTION!'
        return context

class SchoolListView(ListView):
    model = models.School
    # list view creates context dict: model.lower() + _list
    # OR you can change the term from school_list to:
    context_object_name = 'schools'

class SchoolDetailView(DetailView):
    model = models.School
    template_name = 'basic_app/school_detail.html'
    context_object_name = 'school_detail'

class SchoolCreateView(CreateView):
    fields = ('name', 'principal', 'location')
    model = models.School

class SchoolUpdateView(UpdateView):
    fields = ('name', 'principal')
    model = models.School

class SchoolDeleteView(DeleteView):
    model = models.School
    success_url = reverse_lazy('basic_app:list')
