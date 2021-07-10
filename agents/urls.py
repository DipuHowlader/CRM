from django.urls import path
from . import views

app_name ='agents'

urlpatterns = [
    path('', views.agentPage.as_view(), name='agentPage'),
    path('create/', views.createAgent.as_view(), name='createAgent'),
]