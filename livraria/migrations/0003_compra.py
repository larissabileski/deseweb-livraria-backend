# Generated by Django 4.2.4 on 2023-08-11 17:23

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("livraria", "0002_livro_capa"),
    ]

    operations = [
        migrations.CreateModel(
            name="Compra",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "status",
                    models.IntegerField(
                        choices=[
                            (1, "Carrinho"),
                            (2, "Realizado"),
                            (3, "Pago"),
                            (4, "Entregue"),
                        ],
                        default=1,
                    ),
                ),
                (
                    "usuario",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="compras",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
