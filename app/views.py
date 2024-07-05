from django.shortcuts import render

# Create your views here.
from app.models import *
from rest_framework.views import APIView
from app.serializers import *
from rest_framework.response import Response

class ProductCrud(APIView):
    def get(self,request,pk):
        LPO=Product.objects.all()
        MSPO=ProductMS(LPO,many=True)
        return Response(MSPO.data)
    
    def post(self,request,pk):
        rjd=request.data
        PDO=ProductMS(data=rjd)
        if PDO.is_valid():
            PDO.save()
            return Response({'success':'Data is inserted successfully'})
        else:
            return Response({'Failed':'Issues while inserting'})


    def put(self,request,pk):
        rdo=request.data
        instance=Product.objects.get(pk=pk)
        cdo=ProductMS(instance,data=rdo)
        if cdo.is_valid():
            cdo.save()
            return Response({'Update':'Success'})
        else:
            return Response({'Failed':'Fail'})

    def patch(self,request,pk):
        rdo=request.data
        instance=Product.objects.get(pk=pk)
        cdo=ProductMS(instance,data=rdo,partial=True)
        if cdo.is_valid():
            cdo.save()
            return Response({'Update':'Success'})
        else:
            return Response({'Failed':'Fail'})

    def delete(self,request,pk):
        instance=Product.objects.get(pk=pk).delete()
