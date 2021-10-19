from rest_framework import routers
from owner.api import OwnerViewset

router = routers.DefaultRouter()
router.register('api/owner', OwnerViewset, 'owner')

urlpatterns = router.urls #register the path 'api/owner'
