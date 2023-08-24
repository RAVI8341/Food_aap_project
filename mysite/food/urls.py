from django.urls import path
from . import views
# this urlpattern is belongs to food app
app_name = 'food'
urlpatterns = [
    #/
    path('', views.IndexClassView.as_view(),name='index'),
    #/id
    path('<int:pk>/',views.FoodDetails.as_view(),name='detail'),
    # add item
    path('add',views.CreateItem.as_view(), name='create_item'),
    #update item
    path('update/<int:id>/', views.update,name='update'), 
    #delete
    path('delete/<int:id>/', views.delete,name='delete'),
    
]
