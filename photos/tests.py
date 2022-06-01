from django.test import TestCase
from .models import Location,Category
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


