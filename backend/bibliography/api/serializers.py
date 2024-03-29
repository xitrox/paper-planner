from rest_framework import serializers
from ..models import Paper


class PaperSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Paper
        fields = ('id', 'title', 'author', 'journal', 'date', 'pages')
