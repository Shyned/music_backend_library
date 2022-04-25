from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import MusicLibrarySerializer
from .models import Music_library

@api_view(['GET','POST'])
def music_list(request):
    if request.method == "GET":
        music = Music_library.objects.all()
        serializer =MusicLibrarySerializer(music, many = True)
        return Response(serializer.data)

# Create your views here.

@api_view(['GET','PUT','DELETE'])
def music_details(request,pk):
    pass