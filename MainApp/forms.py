from django.forms import ModelForm, Textarea
from MainApp.models import Snippet, Comment

class SnippetForm(ModelForm):
   class Meta:
       model = Snippet
       # Описываем поля, которые будем заполнять в форме
       fields = ['name', 'lang', 'code', 'public']

# Класс формы для добавления коментария к снипету
class CommentForm(ModelForm):
   class Meta:
       model = Comment
       # Описываем поля, которые будем заполнять в форме
       fields = ['text']
       widgets = {
           'text': Textarea(attrs={'class': 'my-class', 'placeholder': 'Комментарий....'})
       }