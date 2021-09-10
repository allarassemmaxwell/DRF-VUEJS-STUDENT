from rest_framework import serializers
from .models import *


class StudentSerializer(serializers.ModelSerializer):
    # cat_name = serializers.CharField(source='category.title', read_only=True)
    class Meta:
        model = Student
        fields = [
            'id',
            'name',
            'age',
            'description',
            'active',
            'timestamp'    
        ]
        
