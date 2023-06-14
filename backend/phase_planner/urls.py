from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import ToDoAPIViewSet, PhaseAPIViewSet, ProjectAPIViewSet, RewardAPIViewSet

router = DefaultRouter()
router.register(r"todo", ToDoAPIViewSet, basename='todo')
router.register(r"phase", PhaseAPIViewSet, basename='phase')
router.register(r"project", ProjectAPIViewSet, basename='project')
router.register(r"reward", RewardAPIViewSet, basename='reward')


urlpatterns = [
    path("", include(router.urls)),]
