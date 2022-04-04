from rest_framework import serializers
from taggit.serializers import (TagListSerializerField,
                                TaggitSerializer)
from space.models import Tutorial

class TutorialSerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField()
    
    class Meta:
        model = Tutorial
        fields = ('id', 'name', 'url', 'tags', 'difficulty', 'time')