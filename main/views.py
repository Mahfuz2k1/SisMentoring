from django.shortcuts import render, redirect
from datetime import datetime
from .forms import MenteeApplicationForm
from .models import Post
from django.shortcuts import get_object_or_404
  
def home(request):
    return render(request, 'home.html', {'year': datetime.now().year})  
# Create your views here.


def blog(request):
    return render(request, 'blog.html', {'year': datetime.now().year})




def one2one(request):
    submitted = False
    if request.method == "POST":
        form = MenteeApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            submitted = True
    else:
        form = MenteeApplicationForm()
    return render(request, 'one2one.html', {'form': form, 'submitted': submitted})


def home(request):
    blog_posts = Post.objects.filter(category='Blog')[:6]
    skill_posts = Post.objects.filter(category='Skill')[:6]
    return render(request, 'home.html', {
        'blog_posts': blog_posts,
        'skill_posts': skill_posts,
        'year': datetime.now().year
    })


def skill_view(request):
    skill_posts = Post.objects.filter(category='Skill')
    return render(request, 'skill.html', {'skill_posts': skill_posts})



def blog_view(request):
    blog_posts = Post.objects.filter(category='Blog')
    return render(request, 'blog.html', {
        'blog_posts': blog_posts,
        'year': datetime.now().year
    })
    
    


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'post_detail.html', {'post': post})
