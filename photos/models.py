from django.db import models
import datetime as dt

# Create your models here.


class Category(models.Model):
    name= models.CharField(max_length=100,null=False, blank=False)

    def __str__(self):
        return self.name

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()
    
    def update_category(self, update):
        self.photo_category = update
        self.save()
        
    def get_category_id(cls,id):
        category = Category.object.get(pk = id)
        return category

class Location(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name

    def saveLocation(self):
        self.save()
    
    def delete_location(self):
        self.delete()
        
    @classmethod
    def get_location_id(cls, id):
        locate = Location.objects.get(pk = id)
        return locate


class Photo(models.Model):
   category= models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
   location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, blank=True)
   image= models.ImageField(null=False, blank=False)
   description = models.TextField()   
#    pub_date = models.DateTimeField(auto_now_add=True, null=True) 

   def __str__(self):
       return self.description

   def savePhoto(self):
       return self.save()

   def updatePhoto(self):
       self.update()

   def deletePhoto(self):
       self.update()

   @classmethod
   def get_photo_by_id(cls, id):
        a_photo = Photo.objects.get(id=id)
        return a_photo

   @classmethod
   def get_all_photos(cls):
        all_photos = Photo.objects.all()
        return all_photos
   @classmethod
   def search_by_category(cls,search_term):
        image = cls.objects.filter(category__name__contains=search_term)
        return image

   
       
    
    

  
