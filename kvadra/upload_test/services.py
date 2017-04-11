# coding: utf8
from .models import Archive


def get_text():
    return list(Archive.objects.order_by('-id').values())


def upload_text(text):
    if not text:
        raise Exception('Текстовое поле не заполнено')

    Archive(text=text).save()

