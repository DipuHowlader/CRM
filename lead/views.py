from django.db.models import query
from django.http import request
from django.shortcuts import render, reverse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import View
from .models import Agent, Lead
from .forms import CreateLeadForm


class leadPage(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        leads = Lead.objects.all()
        return render(request, 'lead/leadpage.html',{'lead':leads})
    # template_name ='lead/leadpage.html'
    # context_object_name = 'lead'

    # def get_queryset(self):
    #     return Lead.objects.filter(user = request.user)


class createLead(LoginRequiredMixin, CreateView):
    template_name = 'lead/createlead.html'
    form_class = CreateLeadForm

    def get_success_url(self) -> str:
        return reverse('lead:leadPage')

class detailLead(LoginRequiredMixin, DetailView):
    template_name = 'lead/detaillead.html'
    context_object_name = 'lead'

    def get_queryset(self):
        return Lead.objects.all()


class updateLead(LoginRequiredMixin, UpdateView):
    template_name = 'lead/updatelead.html'
    form_class = CreateLeadForm

    def get_queryset(self):
        return Lead.objects.all()

    def get_success_url(self) -> str:
        return reverse('lead:leadPage')

class deleteLead(LoginRequiredMixin, DeleteView):
    template_name = 'lead/deletelead.html'

    def get_queryset(self):
        return Lead.objects.all()

    def get_success_url(self) -> str:
        return reverse('lead:leadPage')



