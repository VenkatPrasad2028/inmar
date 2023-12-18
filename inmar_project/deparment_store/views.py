from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import LocationDetails, DepartmentDetails, CategoryDetails, SubCategoryDetails
from .serializers import LocationSerializer, DepartmentSerializer, CategorySerializer, SubCategorySerializer


@api_view(['GET', 'POST'])
def location_list_create(request):
    if request.method == 'GET':
        locations = LocationDetails.objects.all()
        serializer = LocationSerializer(locations, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        user_id = request.user.id
        created_data = {
                    'location_name' : request.data.get('location_name', ''),
                    'created_by_id' : user_id,
                    'updated_by' :user_id

        }
        serializer = LocationSerializer(data=created_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def location_detail(request, location_id):
    try:
        location = LocationDetails.objects.get(location_id=location_id)
    except location.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = LocationSerializer(location)
        return Response(serializer.data)

    elif request.method == 'PUT':
        user_id = request.user.id
        updated_data = {
                    'location_name' : request.data.get('location_name', ''),
                    'created_by_id' : user_id,
                    'updated_by' :user_id

        }        
        serializer = LocationSerializer(location, data=updated_data, context= { 'user_id': user_id})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        location.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



@api_view(['GET', 'POST'])
def department_list_create(request, location_id):
    if request.method == 'GET':
        departments = DepartmentDetails.objects.filter(location_id_id = location_id)
        serializer = DepartmentSerializer(departments, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        user_id = request.user.id
        created_data = {
        'department_name' : request.data.get('department_name', ''),
        'updated_by' :user_id
        }
        serializer = DepartmentSerializer(data=created_data, context= {'location_id': location_id, 'user_id': user_id})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def department_detail(request, location_id, department_id):
    try:
        department = DepartmentDetails.objects.get(location_id_id = location_id, department_id=department_id)

    except department.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DepartmentSerializer(department)
        return Response(serializer.data)

    elif request.method == 'PUT':
        user_id = request.user.id
        updated_data = {
                    'department_name' : request.data.get('department_name', ''),
                    'updated_by' :user_id

        }        
        serializer = DepartmentSerializer(department, data=updated_data,  context= {'location_id': location_id, 'user_id': user_id})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        department.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



@api_view(['GET', 'POST'])
def category_list_create(request, location_id, department_id):
    if request.method == 'GET':
        categorys = CategoryDetails.objects.filter( department_id_id = department_id)
        serializer = CategorySerializer(categorys, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        user_id = request.user.id
        created_data = {
        'category_name' : request.data.get('category_name', ''),
        'updated_by' :user_id
        }
        serializer = CategorySerializer(data=created_data, context= {'department_id': department_id, 'user_id': user_id})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def category_detail(request, location_id, department_id, category_id):
    try:
        category = CategoryDetails.objects.get(department_id_id = department_id, category_id=category_id)
    except category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    elif request.method == 'PUT':
        user_id = request.user.id
        updated_data = {
                    'category_name' : request.data.get('category_name', ''),
                    'updated_by' :user_id

        }        
        serializer = CategorySerializer(category, data=updated_data,  context= {'location_id': location_id, 'user_id': user_id, 'department_id': department_id})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



@api_view(['GET', 'POST'])
def subcategory_list_create(request, location_id, department_id, category_id):
    if request.method == 'GET':
        subcategorys = SubCategoryDetails.objects.filter( category_id_id = category_id)
        serializer = SubCategorySerializer(subcategorys, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        user_id = request.user.id
        created_data = {
        'sub_category_name' : request.data.get('sub_category_name', ''),
        'updated_by' :user_id
        }
        serializer = SubCategorySerializer(data=created_data, context= {'category_id': category_id, 'user_id': user_id})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def subcategory_detail(request, location_id, department_id, category_id, sub_category_id):
    try:
        subcategory = SubCategoryDetails.objects.get(sub_category_id = sub_category_id, category_id_id=category_id)
    except subcategory.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SubCategorySerializer(subcategory)
        return Response(serializer.data)

    elif request.method == 'PUT':
        user_id = request.user.id
        updated_data = {
                    'sub_category_name' : request.data.get('sub_category_name', ''),
                    'updated_by' :user_id
        }     
        serializer = SubCategorySerializer(subcategory, data=updated_data,  context= {'category_id': category_id, 'user_id': user_id, 'department_id': department_id})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

