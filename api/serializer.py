from rest_framework import serializers
from  .models import *
from django.contrib.auth.hashers import make_password

# for You can create dynamic field serializer for this and get the field data dynamically.
# ref:--https://stackoverflow.com/questions/53319787/how-can-i-select-specific-fields-in-django-rest-framework
class DynamicFieldsModelSerializer(serializers.ModelSerializer):
    """
    A ModelSerializer that takes an additional `fields` argument that
    controls which fields should be displayed.
    """

    def __init__(self, *args, **kwargs):
        # Don't pass the 'fields' arg up to the superclass
        fields = kwargs.pop('fields', None)

        # Instantiate the superclass normally
        super(DynamicFieldsModelSerializer, self).__init__(*args, **kwargs)

        if fields is not None:
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields.keys())
            for field_name in existing - allowed:
                self.fields.pop(field_name)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
       model=User
       fields=['id','email','first_name','username','password']

    def create(self, validated_data):
        validated_data['password']=make_password(validated_data['password'])
        print(validated_data['password'])
        return super().create(validated_data)
    

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
       model = Category
       fields=['id','category_name','category_image','featured']

class CitySerializer(serializers.ModelSerializer):
    class Meta:
       model = City
       fields='__all__'

class PlanSerializer(serializers.ModelSerializer):
    user=serializers.SerializerMethodField('user')
    city=serializers.SerializerMethodField('city')
    Category=serializers.SerializerMethodField('category')
    # user=UserSerializer()
    # city=CitySerializer()
    # category=CategorySerializer()

    def user(self,object):
        serializer = UserSerializer(User.objects.filter(id=object.id),many=True)
        return serializer.data

    def city(self,object):
        serializer = CitySerializer(City.objects.filter(id=object.id),many=True)
        return serializer.data

    def category(self,object):
        serializer = CategorySerializer(Category.objects.filter(id=object.id),many=True)
        return serializer.data

    class Meta:
       model = Plan
       fields=['id','title','user','description','plan_datetime','city','postal_code','Category','plan_image']
    #    fields=['id','title','user','description','plan_datetime','city','postal_code','category','plan_image']
    def create(self, validated_data):
        return Plan.objects.create(**validated_data)

    
class PlanCreateSerializer(serializers.ModelSerializer):
    class Meta:
       model = Plan
       fields='__all__'


    