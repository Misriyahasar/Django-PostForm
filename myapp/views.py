from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView,View
from django.contrib.auth.mixins import LoginRequiredMixin
from myapp.forms import PostForm
from myapp.utils import handle_uploaded_file 
from .models import Post
from django.views.generic import View, ListView
from . import models
def home(request):
    count = User.objects.count()
    return render(request, "myapp/home.html", {"count": count})


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = UserCreationForm()
    return render(request, "registration/signup.html", {"form": form})


@login_required
def secret_page(request):
    return render(request, "myapp/secret_page.html")


class SecretPage(LoginRequiredMixin, TemplateView):
    template_name = "myapp/secret_page.html"
    
class PostView(LoginRequiredMixin,View):
    def get(self,request):
        form= PostForm()
        return render(request,"myapp/post.html",{"form":form})

    def post(self,request):
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            # if form.cleaned_data["attachment"]:
            #     handle_uploaded_file(form.cleaned_data["attachment"])
            form.save()
            return redirect('postlistview')
        else:
            return render(request,"myapp/post.html",{"form":form})

class PostListView(LoginRequiredMixin,View):
    def get(self,request):
        form = Post.objects.all()
        return render(request,"myapp/list_view.html",{"form":form})
def listview(request):
    list= Post.objects.all()
    print(list)
    return render(request, "myapp/list_view.html", {"list": list})
