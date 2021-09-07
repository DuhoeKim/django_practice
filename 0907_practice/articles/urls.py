from django.urls import path
from . import views

app_name ='articles'

urlpatterns = [
    # c
    path('create/', views.create, name='create'),

    #r
    path('', views.index, name='index'),
    path('<int:article_pk>/detail/', views.detail, name='detail'),

    #u
    path('<int:article_pk>/update/', views.update, name='update'),
    
    #d
    path('<int:article_pk>/delete', views.delete, name='delete'),
]
