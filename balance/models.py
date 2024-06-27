import uuid

from django.db import models


# fix for mysql
class UUIDField(models.UUIDField):
    def __init__(self, *args, **kwargs):
        kwargs["max_length"] = 36
        super(models.UUIDField, self).__init__(*args, **kwargs)


class Wallet(models.Model):
    label = models.CharField(max_length=50)
    balance = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        if self.balance < 0:
            raise ValueError("balance can not be negative")
        super(Wallet, self).save(*args, **kwargs)


class Transaction(models.Model):
    txid = UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, db_index=True
    )
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE, db_index=True)
