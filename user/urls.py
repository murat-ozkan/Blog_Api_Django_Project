from rest_framework.routers import DefaultRouter
from django.urls import path, include
from user.views import UserView

router = DefaultRouter()
router.register("", UserView)

urlpatterns = router.urls
# veya
# urlpatterns = [
#     path('', include(router.urls)),
# ]