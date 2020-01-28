from django.urls import path
from . import views

urlpatterns = [
    path('', views.getHomePage),
    path('about/', views.getAboutPage),
    path('contact/', views.getContactPage),
    path('blog/', views.getBlogPage),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail')
]
