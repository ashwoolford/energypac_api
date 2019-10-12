from rest_framework import routers
from .api import OpportunityViewSet

router = routers.DefaultRouter()
router.register('api/opportunities', OpportunityViewSet, 'api_test')

urlpatterns = router.urls