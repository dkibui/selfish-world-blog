from django.db import models
from django.utils.text import slugify
from django.conf import settings
from ckeditor_uploader.fields import RichTextUploadingField

User = settings.AUTH_USER_MODEL


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "Categories"


class Blog(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    content = RichTextUploadingField()
    image = models.ImageField(upload_to="uploads/image")
    date_posted = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, default=0, on_delete=models.CASCADE)
    active = models.BooleanField(
        default=False, help_text="Select to Publish. De-Select un-publish"
    )

    class Meta:
        ordering = ["date_posted", "author"]
        verbose_name_plural = "Blogs"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)

        # Check for slug collisions and append numeric counter if necessary
        # counter = 1
        # original_slug = slugify(self.title)
        # while Blog.objects.filter(slug=self.slug).exists():
        #     self.slug = f"{original_slug}-{counter}"
        #     counter += 1

        super(Blog, self).save(*args, **kwargs)


class Article(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
