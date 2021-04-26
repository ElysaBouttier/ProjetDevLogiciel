from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    # BILL
    # Create

    # Read
    path('client/', views.ClientList.as_view()),
    path('client/<int:pk>', views.ClientDetails.as_view()),
    
    # Update

    # Delete
]

urlpatterns = format_suffix_patterns(urlpatterns)
