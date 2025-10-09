from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class PageContent(models.Model):
    PAGE_CHOICES = [
        ('home', 'Home'),
        ('about', 'About'),
        ('tours', 'Tours'),
        ('blog', 'Blog'),
        ('contact', 'Contact'),
    ]
    CONTENT_TYPE_CHOICES = [
        ('text', 'Texte'),
        ('image', 'Image'),
        ('video', 'Vidéo'),
    ]

    page = models.CharField(max_length=20, choices=PAGE_CHOICES)
    title = models.CharField(max_length=255)
    content_type = models.CharField(max_length=10, choices=CONTENT_TYPE_CHOICES)
    content = models.TextField(blank=True)            
    image = models.ImageField(upload_to='page_images/', blank=True, null=True)
    status = models.CharField(
        max_length=10,
        choices=[('draft', 'Brouillon'), ('published', 'Publié'), ('archived', 'Archivé')],
        default='draft'
    )
    author = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    views = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.page} – {self.title}"
