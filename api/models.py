from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())

def url_default():
   return {"url": "http://www.example.com"}


class photo_card(models.Model):
    label = models.CharField(max_length=255, blank=False, unique=True, null=True)
    url = models.URLField(default=url_default)
    swipe_val = models.IntegerField(default=0)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
