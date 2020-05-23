from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.template.defaultfilters import slugify
from django.contrib.humanize.templatetags import humanize
from django.shortcuts import reverse


STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class ConfessionPost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE, related_name='confession_post')
    display_name = models.CharField(max_length=25, null=True, blank=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now= True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="confessionlikes", blank=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
    
    def get_date(self):
        return humanize.naturaltime(self.created_on)

    def get_absolute_url(self):
        return reverse("confession:post-detail", kwargs={
            'slug':self.slug
        })

    @property
    def total_likes(self):
        return self.likes.count()

def get_unique_slug(sender, instance, **kwargs):
    num = 1
    slug = slugify(instance.title)
    unique_slug = slug
    while ConfessionPost.objects.filter(slug=unique_slug).exists():
        unique_slug = '{}-{}'.format(slug, num)
        num += 1
    instance.slug=unique_slug

pre_save.connect(get_unique_slug, sender=ConfessionPost)

class Comment(models.Model):
    post = models.ForeignKey(ConfessionPost, on_delete=models.CASCADE, related_name='comments')
    name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')

    class Meta:
        # sort comments in chronological order by default
        ordering = ('created',)

    def __str__(self):
        return 'Comment by {}'.format(self.name)

    def get_date(self):
        return humanize.naturaltime(self.created_on)