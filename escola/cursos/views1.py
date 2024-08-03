from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# importar as models
from .models import Curso, Avaliacao

# importar os serializers
from .serializers import CursoSerializer, AvaliacaoSerializer


class CursoAPIView(APIView):
    """ API de Cursos tal tal tal """
    def get(self, request):
        cursos = Curso.objects.all()
        serializer = CursoSerializer(cursos, many=True) # noqa - many=True pq estou pegando "all objects"
        return Response(serializer.data)

    def post(self, request):
        serializer = CursoSerializer(data=request.data) # noqa - receber os dados e serializar
        serializer.is_valid(raise_exception=True) # noqa - verificar se estão válidos
        serializer.save()  # salvar
        return Response(serializer.data, status=status.HTTP_201_CREATED) # noqa - prepara uma resposta com os dados salvos e uma resposta HTTP 


class AvaliacaoAPIView(APIView):
    """ API de avaliações tal tal tal """
    def get(self, request):
        avaliacoes = Avaliacao.objects.all()
        serializer = AvaliacaoSerializer(avaliacoes, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AvaliacaoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
