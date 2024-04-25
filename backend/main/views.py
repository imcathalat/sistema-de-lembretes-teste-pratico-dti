from django.shortcuts import render

from .models import Lembrete
from .serializers import LembreteSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class LembreteList(APIView):
    def get(self, request):
        lembretes = Lembrete.objects.all()
        serializer = LembreteSerializer(lembretes, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = LembreteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


