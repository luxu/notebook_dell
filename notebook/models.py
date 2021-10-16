from django.db import models


class Notebook(models.Model):
    title = models.CharField(
        max_length=100
    )
    price_orig = models.CharField(
        'Preço Original',
        max_length=100
    )
    price_dell = models.CharField(
        'Preço com Desconto',
        max_length=100
    )
    discount = models.CharField(
        'Desconto',
        max_length=100
    )
    freight = models.CharField(
        'frete',
        max_length=100
    )
    name_proc = models.CharField(
        'Processador',
        max_length=100
    )
    name_so = models.CharField(
        'Sistema Operacional',
        max_length=100
    )
    name_video_card = models.CharField(
        'Placa de vídeo',
        null=True,
        max_length=100
    )
    name_monitor = models.CharField(
        'Monitor',
        max_length=100
    )
    name_ssd = models.CharField(
        'SSD',
        max_length=100
    )
    name_ram = models.CharField(
        'Memória RAM',
        max_length=100
    )
    description = models.CharField(
        'Descrição',
        max_length=100
    )

    def __str__(self):
        return self.title
