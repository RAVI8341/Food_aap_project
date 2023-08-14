from django.urls import path
from . import views
# this urlpattern is belongs to food app
app_name = 'food'
urlpatterns = [
    #/
    path('', views.index,name='index'),
    #/id
    path('<int:item_id>/',views.detail,name='detail'),
    # add item
    path('add',views.create_item, name='create_item'),
    #update item
    path('update/<int:id>/', views.update,name='update'), 
    #delete
    path('delete/<int:id>/', views.delete,name='delete'),
    
]
