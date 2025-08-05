from .settings import DEBUG


def base(request):
    return (request, 'base.html')