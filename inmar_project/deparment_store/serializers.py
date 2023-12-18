from rest_framework import serializers
from .models import LocationDetails, DepartmentDetails, CategoryDetails, SubCategoryDetails
from django.contrib.auth.models import User

class LocationSerializer(serializers.ModelSerializer):   
    location_name = serializers.CharField(max_length=500)
    class Meta:
        model = LocationDetails
        fields = ['location_name', 'created_by_id', 'updated_by']

    def create(self, validated_data):
        user_id = self.data['updated_by'] # Access the user making the request
        validated_data['created_by_id'] = user_id
        return LocationDetails.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.location_name = validated_data.get('location_name', instance.location_name)
        instance.updated_by = self.context['user_id']
        instance.save()
        return instance

class DepartmentSerializer(serializers.ModelSerializer):   
    department_name = serializers.CharField(max_length=500)
    class Meta:
        model = DepartmentDetails
        fields = ['location_id_id', 'department_name', 'created_by_id', 'updated_by']

    def create(self, validated_data):
        validated_data['updated_by'] = self.context['user_id']
        validated_data['created_by_id'] = self.context['user_id']
        validated_data['location_id_id'] = self.context['location_id']
        return DepartmentDetails.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.department_name = validated_data.get('department_name', instance.department_name)
        instance.updated_by = self.context['user_id']
        instance.save()
        return instance

class CategorySerializer(serializers.Serializer):
    category_name = serializers.CharField(max_length=500)
    class Meta:
        model = CategoryDetails
        fields = '__all__'

    def create(self, validated_data):
        validated_data['updated_by'] = self.context['user_id']
        validated_data['created_by_id'] = self.context['user_id']
        validated_data['department_id_id'] = self.context['department_id']
        return CategoryDetails.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.category_name = validated_data.get('category_name', instance.category_name)
        instance.updated_by = self.context['user_id']
        instance.save()
        return instance



class SubCategorySerializer(serializers.Serializer):
    sub_category_name = serializers.CharField(max_length=500)
    class Meta:
        model = SubCategoryDetails
        fields = '__all__'

    def create(self, validated_data):
        validated_data['updated_by'] = self.context['user_id']
        validated_data['created_by_id'] = self.context['user_id']
        validated_data['category_id_id'] = self.context['category_id']
        return SubCategoryDetails.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.sub_category_name = validated_data.get('sub_category_name', instance.sub_category_name)
        instance.updated_by = self.context['user_id']
        instance.save()
        return instance

