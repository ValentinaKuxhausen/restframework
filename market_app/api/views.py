from rest_framework.decorators import api_view
from rest_framework.response import Response    
from .serializers import MarketSerializer
from market_app.models import Market

@api_view(['GET', 'POST']) # GET ist default
def markets_view(request):

    if request.method == 'GET':
        markets = Market.objects.all()
        serializer = MarketSerializer(markets, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = MarketSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
@api_view(['GET', 'PUT', 'DELETE'])
def market_single_view(request, pk):   # primary key übergeben

    if request.method == 'GET':
        market = Market.objects.get(pk=pk)
        serializer = MarketSerializer(market)
        return Response(serializer.data)
    

    if request.method == 'PUT':
        market = Market.objects.get(pk=pk)  # holen den Market aus der DB   
        serializer = MarketSerializer(market, data=request.data)    # updaten den Market mit den neuen Daten, Daten aus der request
        
        if serializer.is_valid():
            serializer.save()       # save wenn valide
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
        
    if request.method == 'DELETE':
        market = Market.objects.get(pk=pk)
        serializer = MarketSerializer(market)
        market.delete()
        return Response(serializer.data)
