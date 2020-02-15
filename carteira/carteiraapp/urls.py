from django.conf import settings
from django.conf.urls import url, include
from rest_framework import renderers
from rest_framework.routers import DefaultRouter, SimpleRouter

from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token
from rest_framework_swagger.views import get_swagger_view

from . import views

# Create a router and register our viewsets with it.
router = SimpleRouter()
if settings.DEBUG: 
    router = DefaultRouter()

router.register(r'investments', views.LabelViewSet, base_name='investments')
