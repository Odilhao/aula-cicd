from rest_framework import serializers
from .models import Songs

class SongSerializer(serializers.ModelSerializer):

    class Meta:
        model = Songs
        fields = ['pk', 'song', 'artist', 'streamed', 'time']