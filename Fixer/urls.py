from django.urls import path
from Fixer import views
from Fixer.views import *
from django.views.generic.base import *


# app_name = 'Fixer'
urlpatterns = [
    path('',TemplateView.as_view(template_name = 'base_fixer.html')),
    path('book/',views.book),
    path('books/', views.books),
    path('Orders/',views.Orders.listorders),
    path('ool/',views.BookView.as_view()),
    path('Bookss/',views.BookVieww.as_view(
        {
            'get':'list',
            'post':'create',
        }
    )),
    path('Bookss/<int:pk>',views.BookVieww.as_view(
        {
            'get':'retrieve',
            'post':'update',
            'patch':'partial_retrieve',
            'delete':'destroy',
        }
    )),
    path('menu-item/',MenuItems.as_view()),
    path('cateego/',categorysesr.as_view()),
    path('Author/',AuthorView.as_view()),
    path('menu-item/<int:pk>',SingleItemView.as_view()),
    path('order-item/',views.orderItems),
    path('order-item/<int:pk>',views.SingleOrderItem),
    path('category/<int:pk>',views.category_detail, name='category-detail'),  
    path('author/<int:pk>',views.author_detail, name='author-detail'),  

    
]


