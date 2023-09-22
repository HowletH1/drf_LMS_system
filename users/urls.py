from rest_framework.routers import DefaultRouter

from users import views
from users.apps import UsersConfig

app_name = UsersConfig.name

router = DefaultRouter()
router.register('', views.UserViewSet, basename='users')

urlpatterns = router.urls
