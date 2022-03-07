from unicodedata import name
from django.urls import path
from . import views
from .views import detail_view

app_name = 'AppTest'
urlpatterns = [
    path('', views.index, name="index"),
    path('create/', views.createview, name="Create view"),
    path('list/',views.listview, name="List View" ),
    path('<id>', detail_view ),
    path('<id>/edit', views.updateview, name="Edit View"),
    path('<id>/delete', views.deleteview, name="Delete" ),
]