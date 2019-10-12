from api_test.models import Opportunity
from rest_framework import viewsets, permissions
from .serializers import OpportunitySerializer

# Opportunity viewset

class OpportunityViewSet(viewsets.ModelViewSet):
    queryset = Opportunity.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]

    serializer_class = OpportunitySerializer