from django.shortcuts import render
from .models import Transaction,Category,Currency
from rest_framework.generics import ListAPIView
from .serializers import CurrencySerializer,CategorySerializer,TransactionSerializer
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from .permissions import IsAdminOrReadOnly
# Create your views here.just a readonly endpoint(ListApiView)
class CurrencyListAPiView(ListAPIView):
    queryset=Currency.objects.all()
    print(queryset)
    serializer_class = CurrencySerializer
    

# viewsets to expose all http verbs for saving and deletion
class CategoryModelViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    print(queryset)

# Transactional serializers and models
class TransactionModelViewSet(ModelViewSet):
    permission_classes = (IsAdminOrReadOnly,)
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    print(queryset)

    
    