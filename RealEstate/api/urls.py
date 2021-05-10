from django.urls import path
from . import views 

app_name = 'api'


urlpatterns = [
	path('properties/',views.PropertiesAPI.as_view(), name='properties'),
	path('properties/<int:pk>/',views.PropertieAPI,name='propertie'),

	path('blogs/',views.BlogsAPI.as_view(),name="blogs"),
	path('blog/<int:pk>/',views.BlogAPI,name="blog"),

	path('comment/<int:pk>/',views.CommentAPI,name="comment"),

	path('comment/add/<int:pk>/',views.CommentAddAPI,name="comment-add"),
	
	path('blog/update/<int:pk>',views.BlogUpdatAPI,name="blog-update"),
	path('blog/add',views.BlogAddAPI,name="blog-add"),
	path('propertie/update/<int:pk>',views.PropertieUpdatAPI,name="propertie-update"),
	path('blog/delete/<int:pk>',views.BlogDeleteAPI,name="blog-delete"),
	path('propertie/delete/<int:pk>',views.PropertieDeleteAPI,name="propertie-delete"),
	path('propertie/add',views.PropertieAddAPI,name="propertie-update"),

	path('api-token-auth/', views.CustomAuthToken.as_view())
]