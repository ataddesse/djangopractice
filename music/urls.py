

from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
path('music/register', views.UserFormView.as_view(), name='register'),
path('music', views.IndexView.as_view(), name='index'),
    path('music/<int:pk>', views.DetailView.as_view(), name="detail"),
    path('music/album/add', views.AlbumCreate.as_view(), name="album-add"),
    path('music/album/<int:pk>/delete', views.AlbumDelete.as_view(), name="album-delete"),
    path('music/album/<int:pk>', views.AlbumUpdate.as_view(), name="album-update"),
    path('about', views.about, name='about'),
]
