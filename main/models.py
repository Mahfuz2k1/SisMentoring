from django.db import models
from django.utils.text import slugify


class MenteeApplication(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    whatsapp = models.CharField(max_length=30)
    profession = models.CharField(max_length=100)
    country = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    description = models.TextField()
    problems = models.TextField()
    goal_6month = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    CATEGORY_CHOICES = [
        ('Blog', 'Blog'),
        ('Skill', 'Skill'),
    ]

    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='post_images/')
    content = models.TextField(blank=True)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    slug = models.SlugField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)


    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.category} - {self.title}"
