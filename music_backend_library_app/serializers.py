from rest_framework import serializers
from .models import Music_library


class MusicLibrarySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Music_library
        fields = ["id",'title','artist','album','release_date','genre']