from rest_framework import serializers
from core.models import Propreties , Blogs


class PropSerializer(serializers.ModelSerializer):
	class Meta:
		model = Propreties 
		fields = '__all__'


class BlogSerializes(serializers.ModelSerializer):
	class Meta:
		model = Blogs 
		fields = ['title','mini_des','description']
