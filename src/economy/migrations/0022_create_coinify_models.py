# Generated by Django 3.2.7 on 2021-09-04 10:14

import uuid

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("economy", "0021_bank_bankaccount_banktransaction"),
    ]

    operations = [
        migrations.CreateModel(
            name="CoinifyBalance",
            fields=[
                (
                    "uuid",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                (
                    "date",
                    models.DateField(
                        help_text="The balance was recorded at UTC midnight at this date.",
                        unique=True,
                    ),
                ),
                (
                    "btc",
                    models.DecimalField(
                        decimal_places=8, help_text="The BTC balance", max_digits=18
                    ),
                ),
                (
                    "dkk",
                    models.DecimalField(
                        decimal_places=2, help_text="The DKK balance", max_digits=12
                    ),
                ),
                (
                    "eur",
                    models.DecimalField(
                        decimal_places=2, help_text="The EUR balance", max_digits=12
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="CoinifyInvoice",
            fields=[
                (
                    "uuid",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                (
                    "coinify_id",
                    models.IntegerField(
                        help_text="Coinifys internal ID for this invoice"
                    ),
                ),
                (
                    "coinify_id_alpha",
                    models.CharField(
                        help_text="Coinifys other internal ID for this invoice",
                        max_length=20,
                    ),
                ),
                (
                    "coinify_created",
                    models.DateTimeField(help_text="Created datetime in Coinifys end"),
                ),
                (
                    "payment_amount",
                    models.DecimalField(
                        decimal_places=2, help_text="The payment amount", max_digits=12
                    ),
                ),
                (
                    "payment_currency",
                    models.CharField(help_text="The payment currency.", max_length=3),
                ),
                (
                    "payment_btc_amount",
                    models.DecimalField(
                        decimal_places=8,
                        help_text="The payment amount in BTC.",
                        max_digits=18,
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        help_text="The text description of this Coinify invoice"
                    ),
                ),
                (
                    "custom",
                    models.JSONField(
                        blank=True,
                        help_text="Custom JSON data for this invoice",
                        null=True,
                    ),
                ),
                (
                    "credited_amount",
                    models.DecimalField(
                        decimal_places=8,
                        help_text="The amount credited on our Coinify account.",
                        max_digits=18,
                    ),
                ),
                (
                    "credited_currency",
                    models.CharField(
                        help_text="The currency of the credited amount.", max_length=3
                    ),
                ),
                (
                    "state",
                    models.CharField(
                        help_text="The state of this Coinify invoice", max_length=100
                    ),
                ),
                (
                    "payment_type",
                    models.CharField(
                        help_text="The type of payment for this Coinify infoice. Extra means too much was paid on the original payment ID and a new invoice was created instead.",
                        max_length=100,
                    ),
                ),
                (
                    "original_payment_id",
                    models.IntegerField(
                        blank=True,
                        help_text="The original payment id (used when the invoice payment type is 'extra')",
                        null=True,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="CoinifyPayout",
            fields=[
                (
                    "uuid",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                (
                    "coinify_id",
                    models.IntegerField(
                        help_text="Coinifys internal ID for this payout"
                    ),
                ),
                (
                    "coinify_created",
                    models.DateTimeField(
                        help_text="Created datetime in Coinifys end for this payout"
                    ),
                ),
                (
                    "amount",
                    models.DecimalField(
                        decimal_places=8,
                        help_text="The payout amount before fees",
                        max_digits=18,
                    ),
                ),
                (
                    "fee",
                    models.DecimalField(
                        decimal_places=2, help_text="The payout fee", max_digits=12
                    ),
                ),
                (
                    "transferred",
                    models.DecimalField(
                        decimal_places=2,
                        help_text="The transferred amount after fees",
                        max_digits=12,
                    ),
                ),
                (
                    "currency",
                    models.CharField(help_text="The payout currency.", max_length=3),
                ),
                (
                    "btc_txid",
                    models.CharField(
                        blank=True,
                        help_text="The BTC txid (used if this was a BTC payout).",
                        max_length=64,
                        null=True,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.AlterModelOptions(
            name="banktransaction",
            options={
                "get_latest_by": ["date", "created"],
                "ordering": ["-date", "-created"],
            },
        ),
    ]
