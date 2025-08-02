from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    
    path('blog/', views.blog_view, name='blog'),
    path('skill/', views.skill_view, name='skill'),
    path('booking/', views.one2one, name='one2one'),  # ✅ This line is critical
    path('post/<slug:slug>/', views.post_detail, name='post_detail'),
]


