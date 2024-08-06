from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'categories', CategoryView, basename='category')
router.register(r'brands', BrandView, basename='brand')
router.register(r'products', ProductView, basename='product')
router.register(r'productsline', ProductLineView, basename='productline')
router.register(r'productimages', ProductImageView, basename='productimage')
router.register(r'attributes', AttributeView, basename='Attribute')
router.register(r'attributevalues',AttributeValueView, basename='attributevalue')

urlpatterns = [
    path('api/', include(router.urls)),
]


