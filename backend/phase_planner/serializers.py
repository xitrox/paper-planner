
from rest_framework import serializers
from phase_planner.models import To_Do, Phase, Project, Reward


class ToDoSerializer(serializers.ModelSerializer):

    class Meta:
        model = To_Do
        fields = ['to_do_name', 'to_do_description',
                  'to_do_is_done', 'to_do_phase', 'to_do_project']


class PhaseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Phase
        fields = ['phase_name', 'phase_description',
                  'phase_reward', 'phase_further_reading']


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = ['project_name', 'project_description',
                  'project_deadline', 'project_startdate']


class RewardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reward
        fields = ['reward_name', 'reward_description',
                  'reward_picture', 'reward_phase']
