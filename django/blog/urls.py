from django.urls import path # type: ignore
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.blog, name='home'),
    path('post/<int:post_id>/', views.post, name='post'),
    path('exemplo/', views.exemplo, name='exemplo'),
]
