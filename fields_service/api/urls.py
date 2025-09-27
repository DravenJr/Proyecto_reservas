
from rest_framework.routers import DefaultRouter
from .views import FieldViewSet

router = DefaultRouter()
router.register('fields', FieldViewSet)

urlpatterns = router.urls
