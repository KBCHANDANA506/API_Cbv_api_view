from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from app.serializers import *
from app.models import *
from rest_framework.response import Response


@permission_classes([IsAuthenticated])
class Product_Crud(APIView):
    def get(self,request):
        PQS=Product.objects.all()
        PJD=ProductSerializer(PQS,many=True)

        return Response(PJD.data)