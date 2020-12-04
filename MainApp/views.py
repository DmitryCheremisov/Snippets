from django.http import Http404
from django.shortcuts import render, redirect, HttpResponse
from MainApp.models import Snippet, Comment
from MainApp.forms import SnippetForm, CommentForm
from django.contrib import auth
from django.contrib import messages

def get_base_context(request, pagename):
    return {
        'pagename': pagename
    }


def index_page(request):
    context = get_base_context(request, 'PythonBin')
    return render(request, 'pages/index.html', context)


def thanks(request):
    context = get_base_context(request, 'Thanks!!')
    return render(request, 'pages/thanks.html', context)

def add_snippet_page(request):
    if request.method == "GET":
        context = get_base_context(request, 'Добавление нового сниппета')
        form = SnippetForm()
        context["form"] = form
        return render(request, 'pages/add_snippet.html', context)
    elif request.method == "POST":
        form = SnippetForm(request.POST)
        if form.is_valid():
            snippet = form.save()
            if request.user.is_authenticated:
                snippet.user = request.user
                snippet.save()
            return redirect('/thanks/')
        context = get_base_context(request, 'Добавление нового сниппета')
        form = SnippetForm(request.POST)
        context["form"] = form
        return render(request, 'pages/add_snippet.html', context)

def search(request, sn_id=2):
    #context = {"id": sn_id}
    sn = request.POST['snippet_id']
    sform = SnippetForm(request.POST)
        #if form.is_valid():
    context = get_base_context(request, f"'Найден снипет #'{sn}")
    snippet = Snippet.objects.get(id=sn)
    context["snippet"] = snippet
    return render(request, 'pages/search.html', context)


def snippets_page(request):
    context = get_base_context(request, 'Просмотр сниппетов')
    snippets = Snippet.objects.all()
    #snippets = Snippet.objects.filter(Q)
    context["snippets"] = snippets
    context["num_snippets"] = len(snippets)
    print("context = ", context)
    return render(request, 'pages/view_snippets.html', context)


def snippet(request, snippet_id):
    context = get_base_context(request, 'Страница снипета')
    try:
        item = Snippet.objects.get(id=snippet_id)
        comments = item.comment_set.all()
    except Snippet.DoesNotExist:
        raise Http404
    
    
    context['comments'] = comments
    context['comment_form'] = CommentForm()
    context['snippet'] = item
    return render(request, 'pages/snippet.html', context)



def login_page(request):
    context = get_base_context(request, 'Страница авторизации')
    return render(request, 'pages/login.html', context)

def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(request, username=username, password=password)
        if user:
            auth.login(request, user)
            return redirect('/')

        errors = ["Неверный логин или пароль", ""]
        context = get_base_context(request, 'Авторизация')
        context['errors'] = errors
        context['username'] = username
        return render(request, 'pages/login.html', context)

def logout(request):
    auth.logout(request)
    return redirect('/')


def sn_delete(request, sn_id):
    snippet = Snippet.objects.get(id=sn_id)
    snippet.delete()
    return redirect('/')

def edit(request, snippet_id):
    # просмотр и изменение сниппета
    # если пришли по редактированию
    if request.method == "POST":
        # moe
        id = request.POST['id']
        new_name = request.POST["sn_name"]
        new_code = request.POST["sn_code"]
        snippet = Snippet.objects.get(id=id)
        snippet.name = new_name
        snippet.code = new_code
        snippet.save()

        messages.success(request, 'Profile updated successfully')
        # kung-fu master
        #id = request.POST['id']
        #origin = Snippet.objects.get(id=id)
        #snippet = SnippetForm(request.POST, instance=origin)
        #snippet.save()

    context = get_base_context(request, 'Редактирование снипета')
    try:
        item = Snippet.objects.get(id=snippet_id)
    except Snippet.DoesNotExist:
        raise Http404
    context['snippet'] = item
    return render(request, 'pages/edit.html', context)

def comment_add(request):
    if request.method == "POST":
        snippet_id = request.POST['snippet_id']
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            snippet = Snippet.objects.get(id=snippet_id)
            comment.snippet = snippet
            comment.save()

        return redirect(f'/snippet/{snippet_id}')

    raise Http404




#def add_form(request):
#    if request.method == "POST":
        