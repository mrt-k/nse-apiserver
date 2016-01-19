from rest_framework import routers
from api.views import NseViewSet, NseArgvViewSet

router = routers.DefaultRouter()
router.register(r'nse', NseViewSet)
router.register(r'nse_argv', NseArgvViewSet)
