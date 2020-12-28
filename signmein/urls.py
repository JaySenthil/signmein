# signmein/urls.py
from django.urls import path, include
from .views import LoginPageView, SignUpPageView, DashboardPageView, SignInPageView, SuccessPageView, NotFoundView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('orgs/login/', auth_views.LoginView.as_view(), {'template_name': 'login.html'}, name='login'),
    path('orgs/', include('django.contrib.auth.urls')),
    path('orgs/signup/', SignUpPageView, name='signup'),
    path('orgs/dashboard/', DashboardPageView, name='dash'),
    path('meeting/<str:orgname>/signin', SignInPageView, name = 'signin'),
    path('meeting/<str:orgname>/success', SuccessPageView, name = 'success'),
    path('meeting/notfound', NotFoundView, name = 'notfound'),
]
