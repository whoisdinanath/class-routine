from rest_framework import serializers
from .models import Subject


class SubjectSerializer(serializers.ModelSerializer):
    day = serializers.StringRelatedField()
    level = serializers.StringRelatedField()
    category = serializers.StringRelatedField()

    class Meta:
        model = Subject
        fields = ['subject', 'teacher', 'category', 'level', 'group',
                  'day', 'start_time', 'end_time']
