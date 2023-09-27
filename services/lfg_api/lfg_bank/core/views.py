# views.py
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import ConfigurableFields
from .serializers import ProposalSerializer , ConfigurableFieldsSerializer

class ProposalViewSet(viewsets.ViewSet):

    def create(self, request):
        serializer = ProposalSerializer(data=request.data)
        
        if serializer.is_valid():
            proposal = serializer.save()
            return Response(ProposalSerializer(proposal).data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class FieldsViewSet(viewsets.ViewSet):

    def list(self, _):      
        queryset = ConfigurableFields.objects.all().first()
        serializer = ConfigurableFieldsSerializer(queryset, many=False)
        return Response(serializer.data)
