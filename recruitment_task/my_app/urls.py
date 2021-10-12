from rest_framework.routers import DefaultRouter

from my_app.views import CategoryViewSet, OffersViewSet

router = DefaultRouter()
router.register(r"category", CategoryViewSet, basename="category")
router.register(r"offers", OffersViewSet, basename="offer")
urlpatterns = router.urls
