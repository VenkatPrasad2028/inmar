from django.contrib import admin
from .models import LocationDetails, DepartmentDetails, CategoryDetails, SubCategoryDetails

models_to_register = [LocationDetails, DepartmentDetails, CategoryDetails, SubCategoryDetails]

for model in models_to_register:
    admin.site.register(model)
