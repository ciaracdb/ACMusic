from django.contrib.auth.models import User, Group
from rest_framework import serializers

from dbapi.models import Song

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class SongSerializer(serializers.Serializer):
    class Meta:
        model = Song
        fields = ('name', 'url', 'player')

class PlaylistSerializer(serializers.Serializer):
    class Meta:
        model = Song
        fields = ('id', 'name', 'url', 'songs', 'votes')