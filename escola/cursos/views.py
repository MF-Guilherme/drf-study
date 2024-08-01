from rest_framework.views import APIView
from rest_framework.response import Response

# importar as models
from .models import Curso, Avaliacao

# importar os serializers
from .serializers import CursoSerializer, AvaliacaoSerializer


class CursoAPIView(APIView):
    """ API de Cursos tal tal tal """
    def get(self, request):
        cursos = Curso.objects.all()
        serializer = CursoSerializer(cursos, many=True) # many=True pq estou pegando "all objects" # noqa
        return Response(serializer.data)


class AvaliacaoAPIView(APIView):
    """ API de avaliações tal tal tal """
    def get(self, request):
        avaliacoes = Avaliacao.objects.all()
        serializer = AvaliacaoSerializer(avaliacoes, many=True)
        return Response(serializer.data)
