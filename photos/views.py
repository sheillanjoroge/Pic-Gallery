from django.shortcuts import render
from .models import Image, Tag, Location

# Create your views here.
def index(request):
    all_images = Image.get_all_images()
    all_tags = Tag.get_all_tags()
    all_locations = Location.get_all_locations()

    return render(request, 'home.html', {'images': all_images, 'tags': all_tags, 'locations': all_locations})

def show_image(request, id):
    image = Image.get_image(id)    
    link=request.build_absolute_uri()
    return render(request, 'photo.html', {'image': image, 'link': link})

def search(request):
    if 'image' in request.GET and request.GET['image']:
        searched_term = request.GET.get('image')
        images = Image.search_image_by_keyword(searched_term)

        return render(request, 'search.html', {'images': images, 'term': searched_term})

def discover(request):
    tags = Tag.get_all_tags()

    return render(request, 'discover.html', {'tags': tags})

def images_by_tag(request, id):
    images=Image.search_image_by_tag(id)

    return render(request, 'home.html', {'images': images})

def images_by_location(request, id):
    images=Image.search_image_by_location(id)

    return render(request, 'home.html', {'images': images})