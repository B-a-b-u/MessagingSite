from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Post


def home(request):
    posts = Post.objects.all()
    return render(request, "home.html", {"posts": posts})

# view for individual post
def individual_post(request, pk):
    # Check if the user is logged in
    user_post = Post.objects.get(id=pk)
    return render(request, "post.html", {"user_post": user_post})

#  view for deleting a post
def delete_post(request, pk):
    post = Post.objects.get(id=pk)
    post.delete()
    return render(request, "home.html")


# View for adding new post

def add_post(request):
    if request.method == "POST":
        # getting variables from form
        username = request.POST.get("username")
        email = request.POST.get("email")
        caption = request.POST.get("caption")
        content = request.POST.get("content")

        # Adding variables to Database
        new_post = Post()
        new_post.user_name = username
        new_post.email = email
        new_post.caption = caption
        new_post.content = content
        new_post.save()

        return redirect("home")
    return render(request, "add_post.html")

# Views for updating post

def update_post(request, pk):

    # fetching current data
    current_post = Post.objects.get(id=pk)

    if request.method == "POST":
        # getting variables from form
        username = request.POST.get("username")
        email = request.POST.get("email")
        caption = request.POST.get("caption")
        content = request.POST.get("content")

        # updating variables to Database
        current_post.user_name = username
        current_post.email = email
        current_post.caption = caption
        current_post.content = content
        current_post.save()

        return render(request,"home.html")
    return render(request,"update_post.html",{"current_post":current_post})



