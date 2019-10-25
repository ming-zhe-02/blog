from django.http.response import HttpResponse
from django.http import HttpResponse


def main(request):
    '''
    Show 'Hello world!' in the main page
    '''
    return HttpResponse('Hello world!')