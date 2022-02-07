from django.urls import path
from .views import Index ,About,Product,Contact

app_name = 'main'

urlpatterns = [
    path('',Index,name="index"),
    path('about/', About, name="about"),
    path('product/', Product, name="products"),
    path('contact/', Contact, name = "contact")
]