
from rest_framework.routers import DefaultRouter
from .views import RoleViewSet, PermissionViewSet, UserRoleViewSet

router = DefaultRouter()
router.register('roles', RoleViewSet)
router.register('permissions', PermissionViewSet)
router.register('userroles', UserRoleViewSet)

urlpatterns = router.urls
