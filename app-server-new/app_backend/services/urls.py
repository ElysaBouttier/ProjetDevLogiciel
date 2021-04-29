from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    # ------------------------------------------------------------
    # ------------------------BILL-------------------------------- 
    # ------------------------------------------------------------
    path('bill/', views.BillList.as_view()),
    path('bill/<int:pk>', views.BillDetails.as_view()),

    # ------------------------------------------------------------
    # ------------------------CLIENT------------------------------ 
    # ------------------------------------------------------------
    path('client/', views.ClientList.as_view()),
    path('client/<int:pk>', views.ClientDetails.as_view()),

    # ------------------------------------------------------------
    # ------------------------PRODUCT----------------------------- 
    # ------------------------------------------------------------
    path('product/', views.ProductList.as_view()),
    path('product/<int:pk>', views.ProductDetails.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)


