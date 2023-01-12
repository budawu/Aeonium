from django.urls import path
from . import views

app_name = 'aeonium'
urlpatterns = [
    #index page
    path('',views.index,name='index'),
    path('posts/<int:id>/',views.detail,name='detail'),
    path('page/<int:id>/',views.page,name='page')
]
