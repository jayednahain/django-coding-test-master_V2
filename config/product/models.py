from django.db import models

# Create your models here.
class Variant(models.Model):
   title       = models.CharField(max_length=40)
   description = models.TextField()
   active      = models.BooleanField(default=True)
   updated_at  = models.DateTimeField(auto_now=True,null=True,blank=True)
   created_at  = models.DateTimeField(auto_now_add=True,null=True,blank=True)

   def __str__(self):
      return self.title


class Product(models.Model):
   title = models.CharField(max_length=255)
   sku = models.SlugField(max_length=255)
   description = models.TextField()
   updated_at  = models.DateTimeField(auto_now=True,null=True,blank=True)
   created_at  = models.DateTimeField(auto_now_add=True,null=True,blank=True)

   def __str__(self):
      return self.title

class ProductImage(models.Model):
   product    = models.ForeignKey(Product, on_delete=models.CASCADE)
   file_path  = models.URLField()
   updated_at = models.DateTimeField(auto_now=True,null=True,blank=True)
   created_at = models.DateTimeField(auto_now_add=True,null=True,blank=True)


class ProductVariant(models.Model):
   variant_title = models.CharField(max_length=255)
   variant       = models.ForeignKey(Variant, on_delete=models.CASCADE)
   product       = models.ForeignKey(Product, on_delete=models.CASCADE)
   updated_at    = models.DateTimeField(auto_now=True,null=True,blank=True)
   created_at    = models.DateTimeField(auto_now_add=True,null=True,blank=True)

   def __str__(self):
      return self.variant_title


class ProductVariantPrice(models.Model):
   product_variant_one = models.ForeignKey(ProductVariant, on_delete=models.CASCADE,
                                           related_name='product_variant_one')
   product_variant_two = models.ForeignKey(ProductVariant, on_delete=models.CASCADE,
                                           related_name='product_variant_two')
   product_variant_three = models.ForeignKey(ProductVariant,on_delete=models.CASCADE,
                                             related_name='product_variant_three')
   price = models.FloatField()
   stock = models.FloatField()
   product = models.ForeignKey(Product, on_delete=models.CASCADE)
   updated_at = models.DateTimeField(auto_now=True,null=True,blank=True)
   created_at = models.DateTimeField(auto_now_add=True,null=True,blank=True)
