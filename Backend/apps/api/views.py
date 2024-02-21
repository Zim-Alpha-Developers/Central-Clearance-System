# Create your views here.
from rest_framework.views import APIView
from django.shortcuts import redirect, render
from .models import *
from apps.api.serializers import *
from rest_framework.response import Response



def index(request):
    user = request.user
    # Check whether the user is logged in or not
    if user.is_authenticated:
        if user.user_type == 1:
            pass
        elif user.user_type == 2:
            pass
        else:
            return redirect("login")
    else:
        return redirect("login")

class IndividualView(APIView):
    def get(self, request):
        individuals = IndividualDetails.objects.all()
        serializer = IndividualSerializer(individuals, many=True)
        return Response(serializer.data)
        return Response(serialized_data)

    def post(self, request):
        print("IndividualView post")
        serializer = IndividualSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)