from django.shortcuts import render, redirect
from .models import Category, Photo

# Create your views here.
def gallary(request):
    category = request.GET.get('category')
    if category==None:
        photos = Photo.objects.all()
    else:
        photos = Photo.objects.filter(category__name=category)



            
    categories = Category.objects.all()
    context = {'categories' : categories, 'photos' : photos}
    return render(request,'photos/gallary.html', context)

def viewphoto(request, pk):
    photo = Photo.objects.get(id=pk)
    return render(request,'photos/photo.html', {'photo': photo})

def addphoto(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        data = request.POST
        image = request.FILES.get('image')
        
        if data['category'] != 'none':
            category = Category.objects.get(id=data['category'])
        elif data['category_new']!='':
            category, created=Category.objects.get_or_create(name=data['category_new'])
        else:
            category=None
        photo=Photo.objects.create(
            category=category,
            description=data['description'],
            image=image,
        )
        
        return redirect('gallary')
        
    context = {'categories' : categories}
    return render(request,'photos/add.html', context)


def updatephoto(request, pk):
    photo = Photo.objects.get(id=pk)
    categories = Category.objects.all()

    if request.method == 'POST':
        data = request.POST
        image = request.FILES.get('image')
        
        if data['category'] != 'none':
            category = Category.objects.get(id=data['category'])
        elif data['category_new'] != '':
            category, created = Category.objects.get_or_create(name=data['category_new'])
        else:
            category = None
        
        # Update the photo object with new data
        photo.category = category
        photo.description = data['description']
        
        if image:
            photo.image = image
        
        photo.save()
        
        return redirect('gallary')
    
    context = {'photo': photo, 'categories': categories}
    return render(request, 'photos/add.html', context)


def deletephoto(request, pk):
    photo = Photo.objects.get(id=pk)
    photo.delete()
    return redirect('gallary')
    
def deletecategory(request,category_id):
    category_id=int(category_id)
    try:
        category = Category.objects.get(id=category_id)
        photo = Photo.objects.filter(category=category)
        photo.delete()
        category.delete()
        return redirect('gallary')   
    except Category.DoesNotExist:
        return redirect('gallary')
    
    
    context = {'photo': photo, 'category': category}
    return render(request, 'photo/gallary.html', context)
    
        
    
