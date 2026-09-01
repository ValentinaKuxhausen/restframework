from rest_framework.routers import DefaultRouter
from .views import MarketViewSet, SellerViewSet, ProductViewSet

router = DefaultRouter()
router.register('market', MarketViewSet)
router.register('seller', SellerViewSet)
router.register('product', ProductViewSet)

urlpatterns = router.urls
