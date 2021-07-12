from django.contrib import admin
from django.shortcuts import reverse
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from .views import HomeView, SignupView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('lead/', include('lead.urls', namespace='lead')),
    path('agents/', include('agents.urls', namespace='agent')),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', SignupView.as_view(), name='signup'),
]
