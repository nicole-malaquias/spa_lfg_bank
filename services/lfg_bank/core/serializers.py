from .models import Proposal
from rest_framework import serializers
from .tasks import funcao_com_atraso


class ProposalSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Proposal
        fields = '__all__'

    def create(self, validated_data):
        obj = Proposal.objects.create(**validated_data)
        funcao_com_atraso.delay(obj.id)
        return obj

        
class ConfigurableFieldsSerializer(serializers.ModelSerializer):

    def to_representation(self, instance):

        active_fields = instance.active_fields
        all_fields = [ f.name for f in Proposal._meta.fields]
        return {
            'actives':active_fields,
            'all':all_fields
            }