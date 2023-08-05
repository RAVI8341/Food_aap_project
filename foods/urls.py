from django.urls import path
from . import views
app_name = 'foods'
urlpatterns = [
    path('', views.index, name="index"),
    path("item",views.item,name='item'),
    path('<int:item_id>/',views.details,name='details'),
]