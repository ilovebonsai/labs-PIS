from .models import Article
from django.shortcuts import render, redirect
from django.http import Http404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

# Create your views here.
def archive(request):
    return render(request, 'templates/archive.html', {"posts": Article.objects.all()})

def get_article(request, article_id):
    try:
        post = Article.objects.get(id=article_id)
        return render(request, 'article.html', {"post": post})
    except Article.DoesNotExist:
        raise Http404

def create_post(request):
    if request.user.is_authenticated:
        if request.method == "POST":
        # обработать данные формы, если метод POST
            form = {
                'text': request.POST["text"], 'title': request.POST["title"]
            }
        # в словаре form будет храниться информация, введенная пользователем
            if form["text"] and form["title"]:
                # если уже существует статья с таким названием
                if Article.objects.filter(title=form["title"]).exists():
                    form['errors'] = u"Статья с таким названием уже существует"
                    return render(request, 'create_post.html', {'form': form})
        # если поля заполнены без ошибок
                article = Article.objects.create(text=form["text"], title=form["title"], author=request.user)
                return redirect('get_article', article_id=article.id)
            # перейти на страницу поста
            else:
        # если введенные данные некорректны
                form['errors'] = u"Не все поля заполнены"
                return render(request, 'create_post.html', {'form': form})
        else:
        # просто вернуть страницу с формой, если метод GET
            return render(request, 'create_post.html', {})

    else:
        raise Http404

def registration(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = {
                'username': request.POST["username"], 
                'email': request.POST["email"], 
                'password': request.POST["password"]
            }
            if form["username"] and form["password"]:
                try:
                    User.objects.get(username=form["username"])
                    form['errors'] = u"Пользователь с таким именем уже есть"
                    return render(request, 'registration.html', {'form': form})
                except User.DoesNotExist:
                    User.objects.create_user(username=form["username"], email=form["email"], password=form["password"])
                    return redirect('archive')
            else:
                form['errors'] = u"Заполните обязательные поля ввода"
                return render(request, 'registration.html', {'form': form})

        else:
            return render(request, 'registration.html', {})
    else:
        raise Http404

def log_in(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = {
                'username': request.POST["username"],
                'password': request.POST["password"]
            }
            if form["username"] and form["password"]:
                try:
                    User.objects.get(username=form["username"])
                    user = authenticate(username=form["username"], password=form["password"])
                    if user is not None:
                        login(request, user)
                        return redirect('archive')
                    else:
                        form['errors'] = u"Неверный пароль"
                        return render(request, 'log_in.html', {'form': form})
                except User.DoesNotExist:
                    form['errors'] = u"Пользователь с таким именем не существует"
                    return render(request, 'log_in.html', {'form': form})
            else:
                form['errors'] = u"Заполните обязательные поля ввода"
                return render(request, 'log_in.html', {'form': form})
        else:
            return render(request, 'log_in.html', {})
    else:
        raise Http404