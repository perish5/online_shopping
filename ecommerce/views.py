from django.shortcuts import render, get_object_or_404, HttpResponse
from django.views import View
from django.template import loader
from django.views.generic import (
    TemplateView,
    DeleteView,
    UpdateView,
    CreateView,
    ListView,
    DetailView,
)

# Create your views here.
# class About(View):
#     def get(self,request):
#         template ="ecommerce/about.html"
#         return HttpResponse(request,template)
def about(request):
    template = loader.get_template("ecommerce/about.html")
    return HttpResponse(template.render({"active_tab":"about", "request":request}))