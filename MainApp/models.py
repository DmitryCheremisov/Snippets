from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

LANG_CHOICE = [
    ("py", "Python"),
    ("cpp", "C++"),
    ("js", "Javascript"),
]

class Snippet(models.Model):
    name = models.CharField(max_length=100)
    lang = models.CharField(max_length=30, choices=LANG_CHOICE)
    code = models.TextField(max_length=5000)
    creation_date = models.DateTimeField(default=datetime.now())
    user = models.ForeignKey(to=User, on_delete=models.CASCADE,
                        blank=True, null=True)
    public = models.BooleanField(default=False)

    def __str__(self):
        return f"Snippet: {self.name}"
    

class Comment(models.Model):
   text = models.TextField(max_length=1000)
   creation_date = models.DateTimeField(default=datetime.now())
   author = models.ForeignKey(to=User, on_delete=models.CASCADE)
   snippet = models.ForeignKey(to=Snippet, on_delete=models.CASCADE)
