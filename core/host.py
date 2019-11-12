from django.http import HttpRequest
def data(request):
    self.META['HTTP_HOST']
    return HttpResponse("{}".format(request.META['HTTP_HOST']))
