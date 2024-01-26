from rest_framework import serializers
from .models import Post, Author, Category, ContactUs, ContactUsRequest, FAQ, Tag

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields = '__all__'


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Author
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = '__all__'

class ContactUsRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUsRequest
        fields = '__all__'

class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = '__all__'

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'
