from django.shortcuts import render
from django.views import View
from .forms import createAgentForm

from .models import Agent

# agents
class agentPage(View):
    def get(self, request, *args, **kwargs):
        agents = Agent.objects.filter(user = request.user)
        return render(request, 'agents/agent.html',{'agents':agents})

class createAgent(View):
    def get(self, request, *args, **kwargs):
        form = createAgentForm
        return render(request, 'agents/agentcreate.html',{'form':form})
    
    def post(self, request, *args, **kwargs):
        form = createAgentForm(request.POST)
        if form.is_valid():
            agent = form.save(commit=False)
            agent.user = request.user
            agent.save()
        return render(request, 'agents/agentcreate.html',{'form':form})  