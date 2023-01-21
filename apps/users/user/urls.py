"""URL mapping for the User API."""

from django.urls import path

from user import views

app_name = 'user'

urlpatterns = [
  path('', views.UserView.as_view(), name='user'),
  path('', views.UserProfileInfoView.as_view(), name='user' ),
  path('password/', views.UserPasswordView.as_view(), name='user'),
  path('create/', views.CreateUserView.as_view(), name='create'),
  path('login/', views.CreateUserView.as_view(), name='login'),
  path('logout/', views.UserLogoutView.as_view(), name='logout')
]