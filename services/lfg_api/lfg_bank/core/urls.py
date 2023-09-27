from django.urls import include, path
from rest_framework.routers import DefaultRouter
from core import views

app_name = "core"

routers = DefaultRouter()

routers.register(r"proposal", views.ProposalViewSet, basename="proposal")
routers.register(r"fields", views.FieldsViewSet, basename="fields")

urlpatterns = routers.urls