from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import  slugify


# Create your models here.
class Category(models.Model):
    max_length = 128
    name = models.CharField(max_length=max_length, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(unique=True) # Because name is also unique

    class Meta:
        verbose_name_plural = 'Category'

    def __str__(self):  # Just like toString() in Java
        return self.name

    def __unicode__(self):  # For Unicode Support, Python 2.x
        return self.name

    # Slugify Method
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)


class Page(models.Model):
    max_length = 128
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=max_length)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    def __unicode__(self):  # For Unicode Support, Python 2.x
        return self.title


class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance
    user = models.OneToOneField(User)

    # The additional attributes we wish to include
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    # Override the __unicode__() method to return out something meaningful!
    # Remember if you use Python 2.7.x, define __unicode__ too!
    def __str__(self):
        return self.user.username

