from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    is_digital = models.BooleanField(default=False)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL,null=True, blank=True)

    def __str__(self):
        return self.name
    
class ProductLine(models.Model):
    price = models.DecimalField( max_digits=5, decimal_places=2)
    sku = models.CharField( max_length=50)
    stock_qty = models.IntegerField()
    Product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.sku
    

class ProductImage(models.Model):
    name = models.CharField( max_length=50)
    alt_text = models.CharField( max_length=50)
    url = models.ImageField(upload_to='product_images', height_field=None, width_field=None, max_length=None)
    ProductLine = models.ForeignKey(ProductLine, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.ProductLine.sku}"


class Attribute(models.Model):
    name = models.CharField( max_length=50)

    def __str__(self):
        return self.name
    
class AttributeValue(models.Model):
    value = models.CharField( max_length=50)
    Attribute = models.ForeignKey(Attribute,  on_delete=models.CASCADE)

    def __str__(self):
        return self.value
    
    

    