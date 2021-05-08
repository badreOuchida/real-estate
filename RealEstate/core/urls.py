from django.urls import path
from . import views

app_name="app"
urlpatterns = [
    path('',views.Home.as_view(),name='home'),
    path('properties',views.PropretiesClass.as_view(),name="properties"),
    path('propertie/<int:pk>',views.propertie,name="propertie"),
     path('properties/<str:status>',views.PropertiesStatus,name="status"),
    path('blogs',views.BlogsView.as_view(),name="blogs"),
    path('blog_detail/<int:pk>',views.blog,name="blog_detail"),
    path('contact',views.contact,name="contact"),

    #api
   
    path('comment/<int:pk>',views.CommentCreat,name='comment'),

]
