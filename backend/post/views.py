
from .serializers import PostSerializer
from .models import Post
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from wsgiref.util import FileWrapper
import mimetypes
import os
import base64
from django.http import HttpResponse
from rest_framework import status
# Create your views here.

class PostView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request, *args, **kwargs):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        posts_serializer = PostSerializer(data=request.data)
        if posts_serializer.is_valid():
            posts_serializer.save()
            return Response(posts_serializer.data, status=status.HTTP_201_CREATED)
        else:
            print('error', posts_serializer.errors)
            return Response(posts_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ImageView(APIView):
    def get(self, request, image, *args, **kwargs):
        posts = Post.objects.filter(name = image)

        if len(posts) == 0:
            return Response("", status=status.HTTP_400_BAD_REQUEST)

        serializer = PostSerializer(posts, many = True)
        return Response(serializer.data)

class DownloadImageView(APIView):
    def get(self, request, image, *args, **kwargs):
        posts = Post.objects.filter(name = image)

        if len(posts) == 0:
            return Response("", status=status.HTTP_400_BAD_REQUEST)

        img = posts[0]
        filename = "media/post_images/" + img.name + ".png"
        with open(filename, "rb") as f:
            wrapper      = FileWrapper(f)  
            content_type = mimetypes.guess_type(img.name + ".png")[0]  
            response     = HttpResponse(wrapper,content_type=content_type)  
            response['Content-Length']  = os.path.getsize(filename)    
            response['Content-Disposition'] = "attachment; filename=%s" %  img.name + ".png"
            return response