from django.urls import path
from . import views
urlpatterns=[
    path('',views.gallary, name='gallary'),
    path('photo/<str:pk>/',views.viewphoto, name='photo'),
    path('add/',views.addphoto, name='add'),
    path('deletephoto/<str:pk>/', views.deletephoto, name='deletephoto'),
    path('update/<str:pk>/', views.updatephoto, name='updatephoto'),
    path('deletecategory/<int:category_id>/', views.deletecategory, name='deletecategory'),

    
]