from django.test import TestCase

from .models import Tag, Location, Image

class TestTag(TestCase):

    def setUp(self):
        self.a_tag = Tag(name='Minimalism')
        self.a_tag.save()
    
    def test_instance(self):
        self.assertTrue(isinstance(self.a_tag, Tag))
        self.assertEqual(self.a_tag.name, 'Minimalism')
        self.assertGreater(len(Tag.objects.all()), 0)


    def test_save_tag(self):
        self.a_tag.save_tag()

        self.assertGreater(len(Tag.objects.all()), 0)

    def test_edit_tag(self):
        self.a_tag.save_tag()

        self.a_tag.edit_tag(name='Food')

        self.assertEqual(self.a_tag.name, 'Food')

    def test_delete_tag(self):
        self.a_tag.save_tag()

        all_tags = len(Tag.objects.all())
        self.a_tag.delete_tag()
        updated_tags = len(Tag.objects.all())

        self.assertIs(all_tags, 1)
        self.assertIs(updated_tags, 0)

    def test_get_all_tags(self):
        self.a_tag.save_tag()

        tags = Tag.get_all_tags()

        self.assertEqual(len(tags), 1)

    def tearDown(self):
        self.a_tag = None
        Tag.objects.all().delete()


class TestLocation(TestCase):

    def setUp(self):
        self.a_location = Location(name='Carli')
        self.a_location.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.a_location, Location))
        self.assertEqual(self.a_location.name, 'Carli')

        self.assertGreater(len(Location.objects.all()), 0)

    def test_save_location(self):
        self.a_location.save_location()

        self.assertGreater(len(Location.objects.all()), 0)

    def test_edit_location(self):
        self.a_location.save_location()

        self.a_location.edit_location(name='Kasarani')

        self.assertEqual(self.a_location.name, 'Kasarani')

    def test_delete_location(self):
        self.a_location.save_location()

        all_locations = len(Location.objects.all())
        self.a_location.delete_location()
        updated_locations = len(Location.objects.all())

        self.assertIs(all_locations, 1)
        self.assertIs(updated_locations, 0)

    def test_get_image_by_location(cls):
        self.a_location.save_location()

        locations = Location.get_all_locations()

        self.assertEqual(len(locations), 1)
        

    def tearDown(self):
        self.a_location = None
        Location.objects.all().delete()


class TestImage(TestCase):
    
    def setUp(self):
        self.a_location = Location(name='Carli')
        self.a_tag = Tag(name='Minimalism')
        self.a_tag.save()
        self.a_location.save()
        self.an_image = Image(name='Honeypot', description='My desc', location=self.a_location, image_upload='uploads/matt.jpg')

    def test_instance(self):
        self.an_image.save()
        self.an_image.tag.add(self.a_tag)

        self.assertTrue(isinstance(self.an_image, Image))
        self.assertEqual(self.an_image.name, 'Honeypot')
        self.assertTrue(isinstance(self.a_location, Location ))
        self.assertGreater(len(Image.objects.all()), 0)

    def test_save_image(self):
        self.an_image.save_image(self.a_tag)

        self.assertGreater(len(Image.objects.all()), 0)
        self.assertGreater(len(Tag.objects.all()), 0)

    def test_delete_image(self):
        self.an_image.save_image(self.a_tag)

        self.an_image.delete_image()

        self.assertEqual(len(Image.objects.filter(name='Honeypot')), 0)


    def test_update_image(self):
        self.an_image.save_image(self.a_tag)

        self.an_image.update_image(name='Jaganot', description='KoolAid my lads!')

        self.assertEqual(self.an_image.name, 'Jaganot')
        self.assertEqual(self.an_image.description, 'KoolAid my lads!')
        
    def test_get_images(self):
        self.an_image.save_image(self.a_tag)

        all_images = Image.get_all_images()

        self.assertIs(len(all_images), 1)
        
    def test_search_images_by_keyword(self):
        self.an_image.save_image(self.a_tag)

        images = Image.search_image_by_keyword('H')

        self.assertEqual(len(images), 1)


    def test_get_image_by_id(self):
        self.an_image.save_image(self.a_tag)

        image = Image.get_image(self.an_image.id)        

        self.assertTrue(isinstance(image, Image))
        self.assertEqual(self.an_image.id, image.id)

    def test_search_image_by_tag(self):
        self.an_image.save_image(self.a_tag)

        images = Image.search_image_by_tag(self.a_tag.id)

        self.assertEqual(len(images), 1)

    def test_search_image_by_location(self):
        self.an_image.save_image(self.a_tag)

        images = Image.search_image_by_location(self.a_location.id)

        self.assertEqual(len(images), 1)


    def tearDown(self):
        Location.objects.all().delete()
        Tag.objects.all().delete()
        Image.objects.all().delete()
