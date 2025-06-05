from rest_framework import serializers
from .models import Career
from .models import Comment


class CareerModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Career
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Comment
        fields = '__all__'