from django.shortcuts import render, redirect
from datetime import date
from myapp.models import Request, Feedback, User, Comment
from myapp.forms import ReqForm, FeedForm, RegisterUserForm, CommentForm
from django.utils.crypto import get_random_string
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from myapp.forms import CustomAuthenticationForm
import re
from django.shortcuts import redirect
from django.http import HttpResponseRedirect


def index_page(request):
    previous_page = request.META.get('HTTP_REFERER')
    form = RegisterUserForm()
    if request.method == 'POST':
        if 'request' in request.POST:
            today = date.today()
            form = Request(name=request.POST['name'], phone=request.POST['phone'], date=today.strftime('%d.%m.%Y'))
            form.save()
            return redirect('index')
            pass
        elif 'feedback' in request.POST:
            today = date.today()
            form = Feedback(name=request.POST['name'], mail=request.POST['mail'], message=request.POST['message'], date=today.strftime('%d.%m.%Y'))
            form.save()
            return redirect('index')
            pass
        elif 'consultation' in request.POST:
            today = date.today()
            form = Request(name=request.POST['name'], phone=request.POST['phone'], date=today.strftime('%d.%m.%Y'))
            form.save()
            return redirect('index')
            pass
        elif 'register' in request.POST:
            form = RegisterUserForm(request.POST)
            if form.is_valid():
                previous_page = request.META.get('HTTP_REFERER')
                password = form.cleaned_data['password']
                if not is_valid_password(password):
                    form.add_error('password', 'Пароль не соответствует требованиям.')
                    return render(request, 'index.html', {'form': form})
                name = form.cleaned_data['name']
                phone = form.cleaned_data['phone']
                mail = form.cleaned_data['mail']
                username = get_random_string(length=64, allowed_chars='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
                User = get_user_model()
                user = User(name=name, phone=phone, mail=mail, username=username)
                user.set_password(password)
                user.save()
                messages.success(request, 'Аккаунт успешно зарегистрирован!')
                return redirect(previous_page)
            pass

    return render(request, 'index.html', {'form': form, 'user': request.user})

def about_page(request):

    if request.method == 'POST':
        if 'consultation' in request.POST:
            today = date.today()
            form = Request(name=request.POST['name'], phone=request.POST['phone'], date=today.strftime('%d.%m.%Y'))
            form.save()
            return redirect('about')
            pass

    return render(request, 'about.html')

def csgo_page(request):

    comms = Comment.objects.all()
    if request.method == 'POST':
        if 'consultation' in request.POST:
            today = date.today()
            form = Request(name=request.POST['name'], phone=request.POST['phone'], date=today.strftime('%d.%m.%Y'))
            form.save()
            return redirect('csgo')
            pass
        elif 'join' in request.POST:
            today = date.today()
            form = Request(name=request.POST['name'], phone=request.POST['phone'], date=today.strftime('%d.%m.%Y'))
            form.save()
            return redirect('csgo')
            pass
        elif 'comment' in request.POST:
            today = date.today()
            form = Comment(name=request.POST['name'],
                           message=request.POST['message'],
                           date=today.strftime('%d.%m.%Y'))
            form.save()
            return redirect('csgo')

    return render(request, 'csgo.html', context={"comms": comms})

def dota_page(request):
    comms = Comment.objects.all()
    if request.method == 'POST':
        if 'consultation' in request.POST:
            today = date.today()
            form = Request(name=request.POST['name'], phone=request.POST['phone'], date=today.strftime('%d.%m.%Y'))
            form.save()
            return redirect('dota')
            pass
        elif 'join' in request.POST:
            today = date.today()
            form = Request(name=request.POST['name'], phone=request.POST['phone'], date=today.strftime('%d.%m.%Y'))
            form.save()
            return redirect('dota')
            pass
        elif 'comment' in request.POST:
            today = date.today()
            form = Comment(name=request.POST['name'],
                           message=request.POST['message'],
                           date=today.strftime('%d.%m.%Y'))
            form.save()
            return redirect('dota')

    return render(request, 'dota.html', context={"comms": comms})

def fortnite_page(request):
    comms = Comment.objects.all()
    if request.method == 'POST':
        if 'consultation' in request.POST:
            today = date.today()
            form = Request(name=request.POST['name'], phone=request.POST['phone'], date=today.strftime('%d.%m.%Y'))
            form.save()
            return redirect('fortnite')
            pass
        elif 'join' in request.POST:
            today = date.today()
            form = Request(name=request.POST['name'], phone=request.POST['phone'], date=today.strftime('%d.%m.%Y'))
            form.save()
            return redirect('fortnite')
            pass
        elif 'comment' in request.POST:
            today = date.today()
            form = Comment(name=request.POST['name'],
                           message=request.POST['message'],
                           date=today.strftime('%d.%m.%Y'))
            form.save()
            return redirect('fortnite')

    return render(request, 'fortnite.html', context={"comms": comms})

def custom_login(request):
    if request.method == 'POST':
        previous_page = request.META.get('HTTP_REFERER')
        form = CustomAuthenticationForm(request.POST)
        if form.is_valid():
            mail = form.cleaned_data['mail']
            password = form.cleaned_data['password']
            user = authenticate(request, mail=mail, password=password)
            if user is not None:
                login(request, user)
                return redirect(previous_page)
            else:
                form.add_error(None, 'Неверный email или пароль')
    else:
        form = CustomAuthenticationForm()

    return render(request, 'index.html', {'form': form})

def is_valid_password(password):
    if len(password) < 8:
        return False

    if not re.search(r'\d', password):
        return False

    if not re.search(r'[A-Z]', password):
        return False

    if not re.search(r'[a-z]', password):
        return False

    return True

