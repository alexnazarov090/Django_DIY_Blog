from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.fields.related import OneToOneField
from django.urls import reverse


# Create your models here.

class User(AbstractUser):
    pass


class BlogPost(models.Model):
    """A class defining a blog model"""

    # Fields
    title = models.CharField(max_length=100, help_text='Enter a name for a blog post')
    post_date = models.DateField(null=True, blank=True)
    author = models.ForeignKey('BlogAuthor', on_delete=models.SET_NULL, null=True)
    description = models.TextField(max_length=10000, help_text='Type in blog post content')

    # Metadata
    class Meta:
        ordering = ['-post_date']

    # Methods
    def get_absolute_url(self):
        """Returns the url to access a particular instance of Blog post."""
        return reverse('blog:blog-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Blog object (in Admin site etc.)."""
        return self.title


class BlogAuthor(models.Model):
    """A class defining a blog author model"""

    # Fields
    username = OneToOneField(User, on_delete=models.SET_NULL, null=True)
    bio = models.TextField(max_length=1000, help_text='Blog author biography')

    # Methods
    def get_absolute_url(self):
        """Returns the url to access a particular instance of Blog Author(Blogger)."""
        return reverse('blog:blogger-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Blogger object (in Admin site etc.)."""
        return str(self.username)


class Comment(models.Model):
    """A class defining a comment model"""

    # Fields
    post_date = models.DateField(null=True, blank=True)
    description = models.TextField(max_length=1000, help_text='Enter a comment description')
    blog = models.ForeignKey(BlogPost, on_delete=models.SET_NULL, null=True, blank=True)
    commenter = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    # Metadata
    class Meta:
        ordering = ['-post_date']

    # Methods
    def get_absolute_url(self):
        """Returns the url to access a particular instance of Comment."""
        return reverse('blog:blogger-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Comment object (in Admin site etc.)."""
        if len(self.description) >= 75:
            return self.description[0:74]
        return self.description

