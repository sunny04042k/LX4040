from django.urls import path
from django.urls import include
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.index.as_view(), name='code'),
    path('html/<str:path>',views.POST_HTML, name='post_html'),
    url(r'^likes?meta=html$',views.like_post_html, name='like_post_html'),
]
