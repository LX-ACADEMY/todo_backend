from rest_framework import viewsets
from .models import TodoModel
from .serializers import TodoModelSerializer


class TodoModelViewSet(viewsets.ModelViewSet):
    queryset = TodoModel.objects.all()
    serializer_class = TodoModelSerializer
