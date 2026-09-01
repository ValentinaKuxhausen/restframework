from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .serializers import MarketSerializer, SellersDetailSerializer, SellerCreateSerializer, ProductSerializer
from market_app.models import Market, Seller, Product

class MarketViewSet(viewsets.ModelViewSet):
    queryset = Market.objects.all()
    serializer_class = MarketSerializer
    permission_classes = [IsAuthenticated]  # alle Methoden erfordern Login

class SellerViewSet(viewsets.ModelViewSet):
    queryset = Seller.objects.all()
    # kein permission_classes → greift auf globales IsAuthenticatedOrReadOnly zurück

    def get_serializer_class(self):
        if self.request.method in ['POST', 'PUT', 'PATCH']:
            return SellerCreateSerializer
        return SellersDetailSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # kein permission_classes → greift auf globales IsAuthenticatedOrReadOnly zurück
