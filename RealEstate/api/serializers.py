from rest_framework import serializers
from core.models import Propreties , Blogs , Comment ,ListImages


class PropSerializer(serializers.ModelSerializer):
	class Meta:
		model = Propreties 
		fields = '__all__'


class BlogSerializes(serializers.ModelSerializer):
	class Meta:
		model = Blogs 
		fields = '__all__'


class CommentSerializes(serializers.ModelSerializer):
	class Meta:
		model = Comment 
		fields = '__all__'


class ImageSerializer(serializers.ModelSerializer):
	class Meta:
		model = ListImages 
		fields = '__all__'
