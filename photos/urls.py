from django.conf.urls import url


from .views import index, show_image

urlpatterns = [
    url(r'^<int:id>$', show_image, name='show_image')
]
