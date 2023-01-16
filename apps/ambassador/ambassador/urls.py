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
    path('', include(router.urls)),
]
