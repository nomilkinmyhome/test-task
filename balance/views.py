from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from balance.models import Transaction, Wallet
from balance.serializers import TransactionSerializer, WalletSerializer


class TransactionViewSet(viewsets.ModelViewSet):
    serializer_class = TransactionSerializer
    queryset = Transaction.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["txid", "wallet_id"]


class WalletViewSet(viewsets.ModelViewSet):
    serializer_class = WalletSerializer
    queryset = Wallet.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["balance", "label"]
