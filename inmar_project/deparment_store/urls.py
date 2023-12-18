from django.urls import path
from . import views

urlpatterns = [
    path('location/', views.location_list_create),
    path('location/<int:location_id>/', views.location_detail),
    path('location/<int:location_id>/department/', views.department_list_create),
    path('location/<int:location_id>/department/<int:department_id>/', views.department_detail),
    path('location/<int:location_id>/department/<int:department_id>/category/', views.category_list_create),
    path('location/<int:location_id>/department/<int:department_id>/category/<int:category_id>/', views.category_detail),
    path('location/<int:location_id>/department/<int:department_id>/category/<int:category_id>/sub-category/', views.subcategory_list_create),
    path('location/<int:location_id>/department/<int:department_id>/category/<int:category_id>/sub-category/<int:sub_category_id>/', views.subcategory_detail),
    ]