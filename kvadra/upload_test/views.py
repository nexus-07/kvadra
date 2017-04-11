# coding: utf8
import json

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_POST

from .services import get_text, upload_text


@require_POST
def get_text_list(request):
    return HttpResponse(json.dumps(get_text(), ensure_ascii=False), content_type="application/json")


@require_POST
def text_save(request):
    text = request.POST.get('text')
    response = {}
    try:
        upload_text(text)
        response['result'] = 'successful!'
    except Exception as err:
        response['message'] = str(err)
        response['error'] = True

    http_response = HttpResponse(json.dumps(response, ensure_ascii=False), content_type="application/json")
    if response.get('error'):
        http_response.status_code = 500

    return http_response


def index(request):
    return render(request, 'upload_test/index.html')


def text_save_view(request):
    return render(request, 'upload_test/text_save_view.html')
