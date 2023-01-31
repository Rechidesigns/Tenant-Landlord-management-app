from django.shortcuts import render
from .models import Apartment, Tenant
from .serializers import ApartmentSerializer, TenantSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# from account.permissions import IsAdminOrReadOnly
from rest_framework.exceptions import NotFound, PermissionDenied
from rest_framework.decorators import action
from drf_yasg.utils import swagger_auto_schema
from rest_framework_simplejwt.authentication import JWTAuthentication


class AppartmentView(APIView):
    def get(self, request, format=None):
        objs = Apartment.objects.all()
        serializers = ApartmentSerializer(objs, many=True)

        data = {
            "message": "Success",
            "data_count": objs.count(),
            "data": serializers.data
        }

        return Response(data, status=status.HTTP_200_OK)


    @swagger_auto_schema(method= "post", request_body= ApartmentSerializer())
    @action(method=["POST"], detail = True)
    def post(self, request, format=None):
        serializer = ApartmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response({"message":"Success"}, status=status.HTTP_200_OK)

        return Response({"message": "Failed", "error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class ApartmentDetailView(APIView):
    def get_object(self, apartment_id):

        try:
            return Apartment.objects.get(id=apartment_id)
        except Apartment.DoesNotExist:
            raise NotFound(detail = {"message", "apartment not found"})


    def get(self, request, apartment_id, format=None):
            objs = self.get_object(apartment_id)
            serializer = ApartmentSerializer(objs)

            data= {
                "message": "Success",
                "data": serializer.data
            }
            return Response(data, status=status.HTTP_200_OK)


    @swagger_auto_schema(method="put", request_body=ApartmentSerializer())
    @action(methods=["PUT"], detail=True)
    def put(self, request, apartment_id, format=None)
        objs = self.get_object(apartment_id)
        serializers = ApartmentSerializer(objs, data = request.data, partial = True)
        if serializers.is_valid():
            serializers.save()

            return Response({"message":"success"}, status = status.HTTP_200_OK)
        
        return Response({"message":"failed", "error":serializers.errors}, status = status.HTTP_400_BAD_REQUEST)

        
    @swagger_auto_schema(method="delete")
    @action(methods=["DELETE"], detail=True)
    def delete(self, request, apartment_id, formart=None):
        obj = self.get_object(apartment_id)
        if obj.Apartment.count() == 0:
            
            obj.delete()

            return Response(status=status.HTTP_204_NO_CONTENT)
        
        raise PermissionDenied(detail={"message": "cannot delete this house because it contains real Houses."})
