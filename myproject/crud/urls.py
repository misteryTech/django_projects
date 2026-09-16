from django.urls import path
from . import views

urlpatterns = [
    path('insert/', views.insert_data, name='insert_data'),
    path('delete/<int:id>/', views.delete_data, name='delete_data'),
    path('edit/<int:id>/', views.edit_data, name='edit_data'),
]