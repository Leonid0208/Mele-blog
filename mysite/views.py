from django.http import HttpResponseRedirect


def to_blog(request):
    return HttpResponseRedirect('blog/')
