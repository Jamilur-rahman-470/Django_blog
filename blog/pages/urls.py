from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.getHomePage),
    path('about/', views.getAboutPage),
    path('contact/', views.getContactPage),
    path('blog/', views.getBlogPage),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail')
] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
