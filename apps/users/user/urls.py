"""URL mapping for the User API."""

from django.urls import path, include

from user import views

from rest_framework.routers import DefaultRouter

app_name = 'users'

router = DefaultRouter()
router.register('users', views.UsersViewSet)

urlpatterns = [
  path('user/', views.UserView.as_view(), name='user'),
  path('user/password/', views.UserPasswordView.as_view(), name='user'),
  path('user/create/', views.CreateUserView.as_view(), name='create'),
  path('user/login/', views.LoginUserView.as_view(), name='login'),
  path('user/logout/', views.UserLogoutView.as_view(), name='logout'),
  path('user/list/', views.UserListView.as_view(), name='user-list'),
  path('', include(router.urls)),
]