from django.urls import path

from balance.views import TransactionViewSet, WalletViewSet

urlpatterns = [
    path("transactions/", TransactionViewSet.as_view({
        "get": "list",
    })),
    path("wallets/", WalletViewSet.as_view({
        "get": "list",
    })),
]
