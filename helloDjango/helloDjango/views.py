from django.http import HttpResponse

def index(request):
    return HttpResponse(
        'Hello from the Django app!\n',
        content_type='text/plain'
)
