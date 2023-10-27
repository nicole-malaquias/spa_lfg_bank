from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import ConfigurableFields
from .serializers import ProposalSerializer , ConfigurableFieldsSerializer

class ProposalViewSet(viewsets.ViewSet):

    def create(self, request):
        serializer = ProposalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(status=status.HTTP_201_CREATED)

class FieldsViewSet(viewsets.ViewSet):

    def list(self, _):      
        queryset = ConfigurableFields.objects.all().first()
        serializer = ConfigurableFieldsSerializer(queryset, many=False)
        return Response(serializer.data)