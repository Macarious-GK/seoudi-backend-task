from django.urls import path
from Seoudi_Orders.views import *
from Seoudi_Orders import views





urlpatterns = [
    path('items/',views.Items ,name ='items' ),
    path('customers/',views.customer_CR, name= 'customers'),
    path('customers/<int:pk>',views.customer_UD, name= 'customers'),
    path('',views.Orderdetails, name = 'orders'),
]



