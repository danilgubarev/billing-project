from django.urls import path
from . import views

app_name = 'add_tenant'

urlpatterns = [
    path('add-client/', views.AddTenant.as_view(), name='add-client')
]