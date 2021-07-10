from django.urls import path
from . import views

app_name ='lead'

urlpatterns = [
    path('', views.leadPage.as_view(), name='leadPage'),
    path('create/', views.createLead.as_view(), name='leadcreate'),
    path('<int:pk>/detail/', views.detailLead.as_view(), name='leaddetail'),
    path('<int:pk>/update/', views.updateLead.as_view(), name='leadupdate'),
    path('<int:pk>/delete/', views.deleteLead.as_view(), name='leaddelete'),
]