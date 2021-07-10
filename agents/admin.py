from django.contrib import admin
from .models import Agent

class AgentAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'age')

# Register your models here.
admin.site.register(Agent, AgentAdmin)