from django.urls import path,include
from . import views
urlpatterns = [   
    path('get/', views.StudentList.as_view()),
    path('post/', views.StudentCreate.as_view()),
    path('get/<int:pk>/', views.StudentRetrieve.as_view()),
    path('update/<int:pk>/', views.StudentUpdate.as_view()),
    path('delete/<int:pk>/', views.StudentDelete.as_view()),
  
]