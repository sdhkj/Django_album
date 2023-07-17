from django.shortcuts import render
from photo.models import Photo
from django.contrib.auth import authenticate, login, logout
# Create your views here.
from django.http import HttpResponse

# def home(request):
#     # title = '<h1>Hello World</h1>'
#     # return HttpResponse(title)
#
#     # MTV模式中修改
#     photos = Photo.objects.all()
#     context = {'photos': photos}
#     return render(request, 'photo/list.html', context)


def home(request):
    photos = Photo.objects.all()
    context = {'photos': photos}

    # 处理登入登出的POST请求
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user     = authenticate(request, username=username, password=password)
        # 登入
        if user is not None and user.is_superuser:
            login(request, user)
        # 登出
        isLogout  = request.POST.get('isLogout')
        if isLogout == 'True':
            logout(request)

    return render(request, 'photo/list.html', context)