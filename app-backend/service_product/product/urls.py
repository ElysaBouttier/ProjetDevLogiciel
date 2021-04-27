from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    # PRODUCT
    # Create

    # Read
    path('product/', views.ProductList.as_view()),
    path('product/<int:pk>', views.ProductDetails.as_view()),
    
    # Update

    # Delete
]

urlpatterns = format_suffix_patterns(urlpatterns)
