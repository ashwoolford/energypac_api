from rest_framework import serializers
from api_test.models import Opportunity

#Opportunity serializer

class OpportunitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Opportunity
        fields = '__all__'
