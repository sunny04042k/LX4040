from django.conf.urls import url
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    url(r'^login/$',auth_views.LoginView.as_view(template_name='LOGIN/index.html'),name='login'),
    url(r'^logout/$',auth_views.LogoutView.as_view(next_page='/'),name='logout'),
    url(r'^register/$',views.register,name='register'),
    url(r'^profile/$',views.profile_edit,name='profile'),
    url(r'^change_password/$',views.change_password,name='change_password')#FIx
]
