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
        print(serializer)
        print(serializer.is_valid())
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LembreteDelete(APIView):
    def delete(self, request, lembrete_id):
        try: 
            lembrete = Lembrete.objects.get(pk=lembrete_id)
        except Lembrete.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        lembrete.delete()
        return Response({'message': 'Lembrete excluído com sucesso.'}, status=status.HTTP_204_NO_CONTENT)



