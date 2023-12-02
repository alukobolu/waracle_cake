from django.shortcuts import render
from .models import Cake
from .serializers import CakeSerializer
from functools import wraps
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework import status as status_code
from rest_framework.pagination import PageNumberPagination
from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework import generics
# Create your views here.

def try_and_catch(function):
    @wraps(function)
    def wrap(self,request, *args, **kwargs):
        data ={}
        try:
            return function(self,request, *args, **kwargs)
        except Exception as e:
            data["error"]     = f"Sorry something went wrong"
        return Response(data=data,status=status_code.HTTP_400_BAD_REQUEST)
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap

#Pagination default
paginator = PageNumberPagination()
paginator.page_size = 20

class CakeView(generics.GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = CakeSerializer
    delete_param_config = openapi.Parameter(
        'id', in_=openapi.IN_QUERY, description='Cake ID', type=openapi.TYPE_NUMBER)

    @try_and_catch
    def post(self,request):
        """
        Add New Cake
        """
        data = {}
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data["success"] = "Successfully created"
            return Response(data=data, status=status_code.HTTP_201_CREATED)
        else:
            data["error"] = "Invalid Request"
            return Response(data=data, status=status_code.HTTP_400_BAD_REQUEST)

    @try_and_catch
    def get(self,request):
        """
        Get List Of Cakes
        """
        context = []
        cakes = Cake.objects.all()
        for cake in cakes:
            data = {}
            data["id"] = cake.id
            data["name"] = cake.name
            data["comment"] = cake.comment
            data["image"] = cake.imageURL
            data["yumFactor"] = cake.yumFactor
            data["date_created"] = cake.date_created
            context.append(data)
        context = paginator.paginate_queryset(context, request)
        page_response = paginator.get_paginated_response(context)
        return page_response

    @try_and_catch
    @swagger_auto_schema(manual_parameters=[delete_param_config])
    def delete(self,request):
        """
        Delete Cake Record
        """  
        id = request.GET.get('id') 
        cake = Cake.objects.get(id = id)
        cake.delete()
        data = {
            "success":"Successfully Deleted"
        }
        return Response(data=data, status=status_code.HTTP_200_OK)