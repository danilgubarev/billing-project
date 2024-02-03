from django.urls import path, include
from . import views

app_name = 'auth_reg'

urlpatterns = [
    path('login/', views.view_login, name='login'),
    path('login-ajax/', views.AjaxLoginView.as_view(), name='login-ajax'),
    path('signup/', views.view_signup, name='signup'),
    path('signup-ajax/', views.AjaxSignupView.as_view(), name='signup-ajax'),
]