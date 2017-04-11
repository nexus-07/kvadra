# coding: utf8
from django.db import models


class Archive(models.Model):
    """
    хранилище текстов
    """
    text = models.CharField(max_length=50000)  # ограничим текст на всякий пожарный

