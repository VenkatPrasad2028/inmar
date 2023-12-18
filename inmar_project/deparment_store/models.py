from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class BaseModel(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, to_field = 'id' )
    created_timestamp = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length = 100, blank = False, null= False)
    updated_timestamp = models.DateTimeField(auto_now=True) 
    show_flag = models.BooleanField(default=True)

    class Meta:
        abstract = True

class LocationDetails(BaseModel):
    location_id = models.AutoField(primary_key = True)
    location_name = models.CharField(max_length = 500, blank = False, null= False)

    def __str__(self):
        return self.location_name

    class meta:
        db_name = 'location_details'

 
class DepartmentDetails(BaseModel):
    department_id = models.AutoField(primary_key = True)
    location_id = models.ForeignKey(LocationDetails, on_delete=models.CASCADE, to_field='location_id')
    department_name = models.CharField(max_length = 500, blank = False, null= False)

    def __str__(self):
        return self.department_name

    class meta:
        db_name = 'department_details'

 
class CategoryDetails(BaseModel):
    category_id = models.AutoField(primary_key = True)
    department_id = models.ForeignKey(DepartmentDetails, on_delete=models.CASCADE, to_field='department_id')
    category_name = models.CharField(max_length = 500, blank = False, null= False)    

    def __str__(self):
        return self.category_name

    class meta:
        db_name = 'category_details'

 
class SubCategoryDetails(BaseModel):
    sub_category_id = models.AutoField(primary_key = True)
    category_id = models.ForeignKey(CategoryDetails, on_delete=models.CASCADE, to_field='category_id')
    sub_category_name = models.CharField(max_length = 500, blank = False, null= False)   

    def __str__(self):
        return self.sub_category_name

    class meta:
        db_name = 'sub_category_details'

