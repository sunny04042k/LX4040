from django.shortcuts import render
from .models import HTML, CSS, JS
from django.views.generic import ListView, DetailView
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator, PageNotAnInteger
# Create your views here.
class index(ListView):
    queryset = HTML.objects.all().order_by("-date")
    template_name = 'page/index.html'
    context_object_name = "HTML"
def POST_HTML(request,path):
    post  = HTML.objects.get(path=path)
    is_liked = False
    if post.likes.filter(id=request.user.id).exists():
        is_liked = True
    context = {
    'HTML':post,
    'is_liked':is_liked,
    'total_likes':post.total_likes(),
    }
    return render(request,'page/post.html',context)
def like_post_html(request):
    liked_post = get_object_or_404(HTML, id=request.POST.get('post_id'))
    is_liked = False
    if liked_post.likes.filter(id=request.user.id).exists():
        liked_post.likes.remove(request.user)
        is_liked = False
    else:
        liked_post.likes.add(request.user)
        is_liked = True
    return HttpResponseRedirect(liked_post.get_absolute_url())
