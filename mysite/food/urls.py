from django.urls import path
from . import views
# this urlpattern is belongs to food app
app_name = 'food'
urlpatterns = [
    #/
    path('', views.index,name='index'),
    #/id
    path('<int:item_id>/',views.detail,name='detail'),
    
]
