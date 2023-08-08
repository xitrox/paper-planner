from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .api.views import ToDoAPIViewSet, PhaseAPIViewSet, ProjectAPIViewSet, RewardAPIViewSet
from .views import BaseView, PhaseListView, PhaseDetailView
from . import views

router = DefaultRouter()
router.register(r"todo", ToDoAPIViewSet, basename='todo')
router.register(r"phase", PhaseAPIViewSet, basename='phase')
router.register(r"project", ProjectAPIViewSet, basename='project')
router.register(r"reward", RewardAPIViewSet, basename='reward')


urlpatterns = [
    path("", include(router.urls)),
    path("base/", BaseView.as_view()),
    path("phases/", PhaseListView.as_view(), name="phases-list"),
    path("phases/<int:pk>", PhaseDetailView.as_view(), name="phase-detail"),
    path('to-do/cross_off/<to_do_id>', views.cross_off, name='cross_off'),
    path('to-do/uncross/<to_do_id>', views.uncross, name='uncross'),

]
