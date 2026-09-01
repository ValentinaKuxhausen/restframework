from rest_framework import serializers
from market_app.models import Market, Seller, Product

def validate_no_x(value):
    errors = []

    if 'X' in value:
        errors.append('No X allowed')
    if 'Y' in value:
        errors.append('No Y allowed')

    if errors:
        raise serializers.ValidationError(errors)
    return value

class MarketSerializer(serializers.ModelSerializer):
    location = serializers.CharField(max_length=255, validators=[validate_no_x])

    class Meta:
        model = Market
        fields = ['id', 'name', 'location', 'description', 'net_worth']

class SellersDetailSerializer(serializers.ModelSerializer):
    markets = serializers.StringRelatedField(many=True)

    class Meta:
        model = Seller
        fields = ['id', 'name', 'contact_info', 'markets']

class SellerCreateSerializer(serializers.ModelSerializer):
    markets = serializers.PrimaryKeyRelatedField(
        queryset=Market.objects.all(), many=True, write_only=True
    )

    class Meta:
        model = Seller
        fields = ['name', 'contact_info', 'markets']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'market', 'seller']
