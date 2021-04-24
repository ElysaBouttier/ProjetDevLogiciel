from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    # BILL
    # Create

    # Read
    path('bill/', views.BillList.as_view()),
    path('bill/<int:pk>', views.BillDetails.as_view()),
    
    # Update

    # Delete
]

urlpatterns = format_suffix_patterns(urlpatterns)
