from .models import Proposal, ConfigurableFields
from rest_framework import serializers


class ProposalSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Proposal
        fields = '__all__'
        
    def create(self, validated_data):
        return Proposal.objects.create(**validated_data)
    
        
class ConfigurableFieldsSerializer(serializers.ModelSerializer):

    class Meta:
        model = ConfigurableFields
        fields = '__all__'
