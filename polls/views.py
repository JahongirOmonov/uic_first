from django.shortcuts import render
from rest_framework import generics
from .serializers import PostSerializer, AuthorSerializer, CategorySerializer, ContactUsRequestSerializer, TagSerializer, FAQSerializer, ContactUsSerializer
from .models import Post, Author, Category, ContactUs, ContactUsRequest, Tag, FAQ

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
class PostListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetailView(generics.RetrieveAPIView):
    queryset=Post.objects.all()
    serializer_class=PostSerializer
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

class AuthorListView(generics.ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class AuthorDetailView(generics.RetrieveAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetailView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


class ContactUsRequestListView(generics.ListAPIView):
    queryset = ContactUsRequest.objects.all()
    serializer_class = ContactUsRequestSerializer

class ContactUsRequestDetailView(generics.RetrieveAPIView):
    queryset = ContactUsRequest.objects.all()
    serializer_class = ContactUsRequestSerializer
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


class TagListView(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class TagDetailView(generics.RetrieveAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


class FAQListView(generics.ListAPIView):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer

class FAQDetailView(generics.RetrieveAPIView):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

class ContactUsListView(generics.ListAPIView):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer

class ContactUsDetailView(generics.RetrieveAPIView):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>










