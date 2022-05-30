from django.shortcuts import render
from .models import Category, Photo



# Create your views here.

def gallery(request):
    categories = Category.objects.all()
    photos = Photo.objects.all()
    context = {'categories':categories, 'photos':photos}

    return render(request, 'photos/gallery.html', context)


def viewPhoto(request, pk):
    photos = Photo.objects.get(id=pk)
    return render(request, 'photos/photo.html',{'photo':photos})



def addPhoto(request):
    categories = Category.objects.all()

    if request.method == 'POST':
        data = request.POST
        image = request.FILES.get('image')

        print('data:', data)
        print('image:', image)

    context = {'categories':categories,}
    return render(request, 'photos/add.html', context) 