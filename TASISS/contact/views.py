from django.shortcuts import render
from django.views import generic

from .models import Member

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'contact/index.html'
    context_object_name = 'all_member'

    def get_queryset(self):
        return Member.objects.all

class DetailView(generic.DetailView):
    model = Member
    template_name = 'contact/detail.html'
