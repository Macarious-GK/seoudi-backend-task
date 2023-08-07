from django.urls import path,re_path
from Tester import views
from Tester.views import *
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
    path('register/',IndexView.as_view(),name="register"),
    path('new/',views.menu),
    path('home/',views.home, name="home"),
    path('',views.Page2),
    path('login/',views.Page3,name="login"),
    path('books/', first_class_base_views.as_view(), name='book_create'),
    path('room/',views.Room_ApI_view),
    path('class-room/',view_room_API.as_view({'get':'list','post':'create'})),
    path('class-room/<int:pk>',view_room_API.as_view({'get':'retrieve'})),
    path('secret/',views.secret),
    path('api_Token_auth/',obtain_auth_token),
    path('manager/',views.Manager_view),
    path('Trottling/', views.Trottling),
    path('Trottleingauth/',views.Trottleing_auth),
    path('groups/manager/users',views.managers),
    path('ratings/', views.RatingsView.as_view()),    
    
]