"""URL mappings for the ambassador app."""

from django.urls import (
    path,
    include,
)

from rest_framework.routers import DefaultRouter
from ambassador import views


router = DefaultRouter()

app_name = 'ambassador'

urlpatterns = [
    # path('', include(router.urls)),
    path('create/', views.CreateView.as_view(), name='ambassador'),
    path('login/', views.LoginView.as_view(), name='ambassador'),
    path('logout/', views.LogoutView.as_view(), name='ambassador'),
    path('', views.UserView.as_view(), name='ambassador'),
    path('password/', views.ProfilePasswordView.as_view(), name='ambassador'),
    path('users/', views.AmbassadorView.as_view(), name='users')
]
