from unicodedata import name
from django.urls import path
from .views import detail_view
from . import views
# from .views import detail_view

app_name = 'Shop'
urlpatterns = [
    path('',views.listview, name="List View" ),
    path('create/', views.createview, name="Create view"),
    path('<id>', detail_view ),
    path('<id>/edit', views.updateview, name="Edit View"),
    # path('<id>/delete', views.deleteview, name="Delete" ),
]