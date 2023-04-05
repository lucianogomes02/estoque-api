from django.db import models

import uuid
from enum import Enum


class TipoDeProduto(Enum):
    KIT: str = "Kit"
    BARRA: str = "Barra"
    TRUFA: str = "Trufa"
    EVENTO: str = "Evento"

    @classmethod
    def opcoes(cls):
        return (
            ("KIT", cls.KIT.value),
            ("BARRA", cls.BARRA.value),
            ("TRUFA", cls.TRUFA.value),
            ("EVENTO", cls.EVENTO.value),
        )


class Produto(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nome = models.CharField(
        max_length=80,
        blank=False,
        null=False,
    )
    tipo = models.CharField(
        max_length=10,
        choices=TipoDeProduto.opcoes(),
        blank=False,
        null=False,
        default="BARRA",
    )

    def __str__(self):
        return f""
