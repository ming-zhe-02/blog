from django.http.response import HttpResponse
from django.shortcuts import render


def main(request):
    '''
    Show 'Hello world!' in the main page
    '''
    return HttpResponse('Hello world!')
