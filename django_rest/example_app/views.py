from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.


def hello(request):
    return HttpResponse('Hello World!')


@api_view(['GET'])
def hello_rest_api(request):
    data = {'message': 'Hello, REST API'}
    return Response(data)
