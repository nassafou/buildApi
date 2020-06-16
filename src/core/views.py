from django.http import JsonResponse
from django.shortcuts import render

# third party import
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated 
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics

from .serializers import PostSerializer
from .models import Post

class TestView(APIView):
    
    permission_classes = (IsAuthenticated,)
    def get(self, request, *args, **kwargs):
        qs = Post.objects.all()
        post = qs.first()
        serializer = PostSerializer(qs, many=True)
        serializer = PostSerializer(post)
         # data = {
         #     'name': 'jhone',
         #     'age': 23
         # }
        return Response(serializer.data)
        
    def post(self, request, *args, **kwargs):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid(): 
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class PostView(mixins.ListModelMixin,
               mixins.CreateModelMixin,
               generics.GenericAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    
    def get(self, request, *args, **kwargs):
         return self.list(self, request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
         return self.create(request, *args, **kwargs)

class PostCreateView(mixins.ListModelMixin, generics.CreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    
    def get(self, request, *args, **kwargs):
         return self.list(self, request, *args, **kwargs)
        
class PostListCreateView(generics.ListCreateAPIView):        
    serializer_class = PostSerializer
    queryset = Post.objects.all()    
    
   # def perform_create(self, serializer):
        # send an email
    #    serializer.save()
        
          
         

# Create your views here.
# def test_view(request):
#     data = {
#         'name': 'jhone',
#         'age': 23
#     }
#     return JsonResponse(data)

# class TestView(APIView):
#     
#     permission_classes = (IsAuthenticated,)
#     def get(self, request, *args, **kwargs):
#         qs = Post.objects.all()
#         post = qs.first()
#         # serializer = PostSerializer(qs, many=True)
#         serializer = PostSerializer(post)
#          # data = {
#          #     'name': 'jhone',
#          #     'age': 23
#          # }
#         return Response(serializer.data)
#         
#     def post(self, request, *args, **kwargs):
#         serializer = PostSerializer(data=request.data)
#         if serializer.is_valid(): 
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)