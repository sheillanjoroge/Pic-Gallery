from django.db import models

class Location(models.Model):
    name = models.CharField(max_length=100)

    def save_location(self):
        self.save()

    def edit_location(self, **fields):
        for field in fields:
            if dir(self).count(field) > 0:
                setattr(self, field, fields.get(field))

    @classmethod
    def get_all_locations(cls):
        return Location.objects.all()


    def delete_location(self):
        self.delete()


    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=50)

    def save_tag(self):
        self.save()

    def edit_tag(self, **fields):
        for field in fields:
            if dir(self).count(field) > 0:
                setattr(self, field, fields.get(field))

    def delete_tag(self):
        self.delete()

    @classmethod
    def get_all_tags(cls):
        return Tag.objects.all()


    def __str__(self):
        return self.name

class Image(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag)
    upload_date = models.DateField(auto_now_add=True)
    image_upload = models.ImageField(upload_to='uploads/')

    def save_image(self, tag):
        self.save()
        self.tag.add(tag)

    def delete_image(self):
        Image.objects.filter(name=self.name).delete()

    def update_image(self, **attrs):
        image_to_update = Image.objects.filter(name=self.name)
        for attr in attrs:
            if dir(self).count(attr) > 0:
                setattr(self, attr, attrs.get(attr))
            
        self.save()

    @classmethod
    def get_all_images(cls):
        return Image.objects.all()

    @classmethod
    def get_image(cls, id):
        image = Image.objects.filter(id=id)
        
        return image[0]

    @classmethod
    def search_image_by_keyword(cls, keyword):
        return Image.objects.filter(name__icontains=keyword)



    @classmethod 
    def search_image_by_tag(cls, tag):
        return Image.objects.filter(tag=tag)


    @classmethod
    def search_image_by_location(cls, location):
        return Image.objects.filter(location=location)


    def __str__(self):
        return self.name

