from django.test import TestCase
from .models import Location,Category,Photo
import datetime as dt

# Create your tests here.


class LocationTestClass(TestCase):
    def setUp(self):
        self.Turkana = Location(location='Turkana')
        self.Turkana.save_location()

    def test_instance(self):
        self.assertTrue(isinstance(self.Turkana,Location))
    
    def test_updating_location(self):
        location = Location.get_location_id(self.Kisumu.id)
        location.update_location('Kisumu')
        location = Location.get_location_id(self.Kericho.id)
        self.assertTrue(location.location == 'Kericho')
    

        
class CategoryTestClass(TestCase):
    def setUp(self):
        self.food = Category(category='')
        self.food.save_category()

    def test_instance(self):
        self.assertTrue(isinstance(self.food,Category))
    
    def tearDown(self):
        self.food.delete_category()

class PhotoTestCase(TestCase):
     def setUp(self):
        self.Pets = Category(name='Pets')
        self.Pets.save_category()

        self.new_image.Category.add(self.new_category)
        self.new_image.Location.add(self.new_location)

        self.new_location = Location(name='Kisumu')
        self.new_location.save()

     def tearDown(self):
         Photo.objects.all().delete()
         Category.objects.all().delete()
         Location.objects.all().delete()
       

     def test_deletePhoto(self):
            
        self.new_image.deleteImage()
        image = Photo.objects.all()
        self.assertEqual(len(image),0 )

    
     def test_get_all_photos(self):
        all_photos = Photo.get_all_photos()
        self.assertTrue(len(all_photos)>0)
        
     def test_get_photo_by_id(self):
        test_id=1
        a_photo = Photo.objects.filter(test_id)
        self.assertTrue(len(a_photo)>0)