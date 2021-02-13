from django.urls import path

from collection import views

app_name = 'collection'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:item_id>/', views.details, name='details'),
]
