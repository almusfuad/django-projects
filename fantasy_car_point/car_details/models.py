from django.db import models
from django.core.validators import MaxValueValidator
from django.utils.text import slugify

# Create your models here.
class Brand(models.Model):
      brand_name = models.CharField(max_length = 20)
      
      def __str__(self):
            return self.brand_name

def car_image_upload(instance, filename):
      return f'car_details/media/uploads/{instance.brand.brand_name}/{filename}'


class CarModel(models.Model):
      brand = models.ForeignKey(Brand, on_delete = models.CASCADE)
      model_name = models.CharField(max_length = 30)
      model_year = models.IntegerField()
      color = models.CharField(max_length = 20, blank=True)
      car_details = models.TextField()
      price = models.FloatField()
      quantity = models.IntegerField(null = True, blank = True)
      image = models.ImageField(upload_to = car_image_upload, blank = False, null = False)
      slug = models.SlugField(max_length = 255, unique = True, null = True, blank = True)
      
      def generate_product_name(self):
            return f'{self.brand.brand_name} {self.model_name} {self.model_year} {self.color}'
      
      def save(self, *args, **kwargs):
            if not self.slug:
                  base_slug = slugify(f'{self.brand.brand_name}-{self.model_year}-{self.model_name}-{self.color}')
                  self.slug = base_slug
                  counter = 1
                  
                  while CarModel.objects.filter(slug = self.slug).exclude(id = self.id).exists():
                        self.slug = f'{base_slug}-{counter}'
                        counter += 1
            
            super().save(*args, **kwargs)
      
      def __str__(self):
            return f'{self.brand} {self.model_year} {self.model_name}'