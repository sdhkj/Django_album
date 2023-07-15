from django.shortcuts import render
from photo.models import Photo
# Create your views here.
from django.http import HttpResponse

def home(request):
    # title = '<h1>Hello World</h1>'
    # return HttpResponse(title)

    # MTV模式中修改
    photos = Photo.objects.all()
    context = {'photos': photos}
    return render(request, 'photo/list.html', context)