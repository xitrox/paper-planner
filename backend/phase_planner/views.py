from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import ToDoSerializer, PhaseSerializer, ProjectSerializer, RewardSerializer
from .models import To_Do, Phase, Project, Reward


# Create your views here.

class ToDoAPIViewSet(viewsets.ModelViewSet):
    # user später einbinden:
    # def get_queryset(self):
    #     user = self.request.user
    #     return To_Do.objects.filter(owner=user)

    queryset = To_Do.objects.all()

    serializer_class = ToDoSerializer
    # permission_classes = [IsAuthenticated]

    # user später einbinden:
    # def perform_create(self, serializer):
    #     serializer.save(owner=self.request.user)


class PhaseAPIViewSet(viewsets.ModelViewSet):
    queryset = Phase.objects.all()

    serializer_class = PhaseSerializer


class ProjectAPIViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()

    serializer_class = ProjectSerializer


class RewardAPIViewSet(viewsets.ModelViewSet):
    queryset = Reward.objects.all()

    serializer_class = RewardSerializer
