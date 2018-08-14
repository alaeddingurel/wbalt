from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import TextFile
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views import generic
from django.views.generic import View
from .forms import UserForm
import itertools


# Create your views here.

@login_required(login_url='http://localhost:8000/accounts/login')
def index(request):
    all_texts = TextFile.objects.all()
    context = {'all_texts': all_texts}
    return render(request, 'classify/index.html', context)

@login_required(login_url='http://localhost:8000/accounts/login')
def detail(request, text_id):
    username = request.user.username
    all_texts = TextFile.objects.get(pk=text_id)
    # text_json = TextFile.objects.get(pk=text_id).info
    text_json = all_texts.info
    is_protest = None
    if text_json[username] == True:
        is_protest = True
    elif text_json[username] == False:
        is_protest = False
    else:
        is_protest = None
    import re
    context = {'all_texts': all_texts,
               'url_link': re.search(r'http.+\s', str(all_texts)).group(0),
               'is_protest': is_protest}
    return render(request, 'classify/detail.html', context)

@login_required(login_url='http://localhost:8000/accounts/login')
def filtered(request):
    username = request.user.username
    # İşaretlenmemiş datalardan biri verilecek.
    # İşaretlenmiş ilk eleman veriliyor.
    all_new_texts = TextFile.objects.filter(info__contains={username: None})[0]
    context= {'all_new_texts': all_new_texts}
    return render(request, 'classify/filtered.html', context)

@login_required(login_url='http://localhost:8000/accounts/login')
def agreed(request):
    username = request.user.username
    all_new_texts = TextFile.objects.filter(info__contains={username: None})[0]
    all_new_texts.info[username] = True
    all_new_texts.save()
    context = {'all_new_texts': all_new_texts}
    #return render(request, 'classify/agreed.html', context)
    return redirect('filtered')

@login_required(login_url='http://localhost:8000/accounts/login')
def nonagreed(request):
    username = request.user.username
    all_new_texts = TextFile.objects.filter(info__contains={username: None})[0]
    all_new_texts.info[username] = False
    all_new_texts.save()
    context = {'all_new_texts': all_new_texts}
    #return render(request, 'classify/nonagreed.html', context)
    return redirect('filtered')

@login_required(login_url='http://localhost:8000/accounts/login')
def protest(request, text_id):
    username = request.user.username
    all_new_texts = TextFile.objects.get(pk=text_id)
    all_new_texts.info[username] = True
    all_new_texts.save()
    context = {'all_new_texts': all_new_texts}
    #return render(request, 'classify/changeprotest.html', context)
    return redirect('tagged')

@login_required(login_url='http://localhost:8000/accounts/login')
def nonprotest(request, text_id):
    username = request.user.username
    all_new_texts = TextFile.objects.get(pk=text_id)
    all_new_texts.info[username] = False
    all_new_texts.save()
    context = {'all_new_texts': all_new_texts}
    #return render(request, 'classify/changenonprotest.html', context)
    return redirect('tagged')

@login_required(login_url='http://localhost:8000/accounts/login')
def tagged(request):
    username = request.user.username
    all_true_texts = TextFile.objects.filter(info__contains={username: True})
    context = {'all_true_texts': all_true_texts}
    return render(request, 'classify/tagged.html', context)

@login_required(login_url='http://localhost:8000/accounts/login')
def nplabel(request):
    username = request.user.username
    all_false_texts = TextFile.objects.filter(info__contains={username: False})
    context = {'all_false_texts': all_false_texts}
    return render(request, 'classify/nplabel.html', context)

@login_required(login_url='http://localhost:8000/accounts/login')
def conflict(request):
    username = request.user.username
    if username == 'cagri':
        all_diff_texts = TextFile.objects.filter(info__contains={'baglan': False, 'balacan': True})
        all_new_diff_texts = TextFile.objects.filter(info__contains={'baglan': True, 'balacan': False})
        all_texts = all_new_diff_texts | all_diff_texts
        context = {'all_texts': all_texts}
    return render(request, 'classify/conflict.html', context)





class UserFormView(View):
    form_class = UserForm
    template_name = 'classify/registration_form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user = authenticate(username=username, password=password)

            if user is not None:

                if user.is_active:
                    login(request, user)
                    return redirect('classify/')

        return render(request, self.template_name, {'form': form})
