from django.db import models
from django.template.defaultfilters import  slugify


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
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
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    def __unicode__(self):  # For Unicode Support, Python 2.x
        return self.title
