from rest_framework import serializers
from core.models import Propreties , Blogs , Comment


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
