from unicodedata import name
from django.urls import path,include
from .views import *

from rest_framework import permissions

urlpatterns = [
    # user urls

    path('user-create/',UserApiView.as_view(),name="user-create"),

    path('user-list/',UserApiView.as_view(),name="user-list"),
    path('user-login/',UserLoginView.as_view(),name="user-login"),

    # category urls

    path('category-create/',CategoryApiView.as_view(),name="category-create"),
    path('category-list/',CategoryApiView.as_view(),name="category-list"),

    # city urls
    path('city-create/',CityApiView.as_view(),name="city-create"),
    path('city-list/',CityApiView.as_view(),name="city-list"),
    
    # plan urls
    path('plan-create/',PlanCreateApiView.as_view(),name="plan-create"),
    path('plan-list/',PlanListAPIView.as_view(),name="plan-list"),
    path('plan-filter/',PlanFilterApi.as_view(),name="plan-filter"),
    
    # celerty url
    path('test_celery/',test_celery,name="test_celery"),

]
