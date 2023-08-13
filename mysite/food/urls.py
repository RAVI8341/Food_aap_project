from django.urls import path
from . import views
urlpatterns = [
    #/
    path('', views.index,name='index'),
    #/id
    path('<int:item_id>/',views.detail,name='detail'),
    
]
