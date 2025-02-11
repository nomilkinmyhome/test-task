# Generated by Django 5.0.6 on 2024-06-27 18:24

import balance.models
import uuid
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("balance", "0002_rename_wallet_id_transaction_wallet"),
    ]

    operations = [
        migrations.AlterField(
            model_name="transaction",
            name="txid",
            field=balance.models.UUIDField(
                db_index=True,
                default=uuid.uuid4,
                editable=False,
                primary_key=True,
                serialize=False,
            ),
        ),
    ]
