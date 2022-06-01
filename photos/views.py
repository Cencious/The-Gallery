from django.shortcuts import render, redirect
from .models import Category, Photo, Location



# Create your views here.

def gallery(request):
    photos= Photo.objects.all()
    categories = Category.objects.all()
    # location = request.GET.get('location')
    category = request.GET.get('category')
    # print('category:', category)
    # check if there is data in the gallery category

    if category ==None:
       photos = Photo.objects.all()
    else:
        # photos = Photo.objects.filter(location__location=location)
         photos = Photo.objects.filter(category__name=category)

    # locations = Location.objects.all()
    categories = Category.objects.all()
    
    context = {'categories':categories, 'photos':photos, }

    return render(request, 'photos/gallery.html',context)


def viewPhoto(request, pk):
    photos = Photo.objects.get(id=pk)

    return render(request, 'photos/photo.html',{'photo':photos,})



def addPhoto(request):
    categories = Category.objects.all()

    if request.method == 'POST':
        data = request.POST
        image = request.FILES.get('image')

        # print('data:', data)
        # print('image:', image)

        if data['category'] != 'none':
            category = Category.objects.get(id=data['category'])

        elif data['category_new'] != '':
            category,created = Category.objects.get_or_create(name=data['category_new'])

        else:
            category = None
        
        photo = Photo.objects.create(
            category=category,
            description=data['description'],
            image = image
        )
        return redirect('gallery')

    context = {'categories':categories,}
    return render(request, 'photos/add.html', context) 

def searchPhoto(request):

    if 'photo' in request.GET and request.GET["photo"]:
        search_term = request.GET.get("photo")
        searched_photos = Photo.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'photos/search.html',{"message":message,"photos": searched_photos})

    else:
        message = "You haven't searched for any term"
        return render(request, 'photos/search.html',{"message":message})