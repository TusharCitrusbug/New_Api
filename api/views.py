import requests
import datetime
from lib2to3.pgen2 import token
from multiprocessing import AuthenticationError
from webbrowser import get
from django.http import JsonResponse
from rest_framework.response import Response
from django.shortcuts import render
import jwt

from rest_framework.pagination import PageNumberPagination,BasePagination

from api.my_jwt.jwt import my_key
from .models import *
from .serializer import *
from django.contrib.auth.hashers import make_password,check_password
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
from api.task import send_email
from rest_framework.parsers import JSONParser,FormParser
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from api.my_jwt import *
from api.my_token_generator import *
from rest_framework.generics import ListAPIView,ListCreateAPIView
from django.contrib.auth.models import User, auth
from api.my_jwt import my_encode
# command to start celery

# celery -A <project_name.celery> worker -l info

# def jwt_auth(request):
#     try:
#         print(request.META,"982492849284928492489248948924892849248928492849248294")
#         jwt_token = request.META.get('HTTP_AUTHORIZATION')
#         payload=jwt.decode(jwt_token,'secrate',algorithms=['HS256'])
#         return payload
#     except:
#         return None

def test_celery(request):
    send_email.delay()
    return JsonResponse({'done':"success"})

def jwt_authentication(request):
    if request.META.get('HTTP_AUTHORIZATION') != request.COOKIES.get('jwt'):
       return None
    jwt_token = request.META.get('HTTP_AUTHORIZATION')
    return my_decode(jwt_token)
            
class MyPagination(PageNumberPagination):
    page_size=10
    page_query_param ='p'
    page_size_query_param='records'
    

class UserApiView(ListCreateAPIView):
    queryset =User.objects.all()
    serializer_class= UserSerializer
    pagination_class=MyPagination
    MyPagination.page_size=3

    def get_queryset(self):
        return super().get_queryset()
    

# using PYJWT

# class UserLoginView(ListAPIView ):
#     @csrf_exempt
#     def post(self,request):
#         email=request.data['email']
#         password=request.data['password']
#         user=User.objects.filter(email=email).first()
#         if user is not None:
#             if check_password(password,user.password):
#                 payload={
#                     'id':user.id,
#                     "exp":datetime.datetime.utcnow() + datetime.timedelta(minutes=50),
#                     'iat': datetime.datetime.utcnow(),
#                 }
                
#                 token=jwt.encode(payload,'secrate',algorithm='HS256')
#                 response = Response()
#                 response.set_cookie(key='jwt',value=token,httponly=True)
#                 response.data ={
#                     'jwt':token
#                 }
#                 return response
#             else:
#                 return JsonResponse({'password-error':"password is incorrect enter again"})
#         else:
#             return JsonResponse({'authentication-error':"User does not exists"})


class UserLoginView(ListAPIView):
    @csrf_exempt
    def post(self,request):
        email=request.POST.get('email')
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=User.objects.filter(username=username).first()
        if user is not None:
            if email == user.email:
                if check_password(password,user.password):
                    s = requests.session()
                    s.cookies.clear()
                    payload = {'user': user.id}
                    token=my_encode(payload=payload)
                    response = Response()
                    response.set_cookie(key='jwt',value=token,httponly=True)
                    response.data ={
                        'jwt':token
                    }
                    return response
                else:
                    return Response("password error")
            else:
                return Response("email is not correct")
        else:
            return Response("please provide credentials")
        
        
class CategoryApiView(ListCreateAPIView):
    queryset =Category.objects.all()
    serializer_class= CategorySerializer
    pagination_class=MyPagination
    MyPagination.page_size=3
    def post(self, request, *args, **kwargs):
        # if jwt_authentication(request) is None:
        #     return JsonResponse({'authentication-error':"You have no tocken or your token is expired : please login first to generate token"})
        # else:
            return self.create(request, *args, **kwargs)
    def get(self, request, *args, **kwargs):
        
        # if jwt_authentication(request) is None:
        #     return JsonResponse({'authentication-error':"You have no tocken or your token is expired : please login first to generate token"})
        # else:
            return self.list(request, *args, **kwargs)

class CityApiView(ListCreateAPIView):
    queryset =City.objects.all()
    serializer_class= CitySerializer
    pagination_class=MyPagination
    MyPagination.page_size=3
    def post(self, request, *args, **kwargs):
        # if jwt_authentication(request) is None:
        #     return JsonResponse({'authentication-error':"You have no token or your token is expired : please login first to generate token"})
        # else:
            return self.create(request, *args, **kwargs)

class PlanCreateApiView(ListCreateAPIView):
    queryset =Plan.objects.all()    
    serializer_class= PlanCreateSerializer
    pagination_class=MyPagination
    MyPagination.page_size=3
    # def post(self, request, *args, **kwargs):
    #     if jwt_authentication(request) == None:
    #         return JsonResponse({'authentication-error':"You have no tocken or your token is expired  : please login first to generate token"})
    #     else:
    #         send_email.delay(request.data)
    #         return self.create(request, *args, **kwargs)
    def post(self, request, *args, **kwargs):
        send_email.delay(request.data)
        return self.create(request, *args, **kwargs)

class PlanListAPIView(ListAPIView):
    queryset =Plan.objects.filter(is_active=False)    
    serializer_class= PlanCreateSerializer
    pagination_class=MyPagination
    MyPagination.page_size=3
    def get(self, request, *args, **kwargs):
        # if jwt_authentication(request) is None:
        #      return JsonResponse({'authentication-error':"You have no tocken or your token is expired : please login first to generate token"})
        # else:
            return self.list(request, *args, **kwargs)
    

class PlanFilterApi(ListAPIView):
    queryset =Plan.objects.all()    
    serializer_class= PlanSerializer
    pagination_class=MyPagination
    MyPagination.page_size=3
    filter_backends = [SearchFilter]
    search_fields = ['title', 'category__category_name']
    # filterset_fields = ['is_active']
    def get_queryset(self):
        return Plan.objects.filter(plan_datetime__contains=self.request.GET.get('plan_date')).exclude(is_active=False)

    def get(self, request, *args, **kwargs):
        if jwt_authentication(request) is None:
             return JsonResponse({'authentication-error':"You have no tocken or your token is expired : please login first to generate token"})
        else:
            return self.list(request, *args, **kwargs)
    