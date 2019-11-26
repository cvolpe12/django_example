from django.shortcuts import render
# from django.http import HttpResponse
# from AppTwo.models import User
from AppTwo.forms import NewUserForm
from django.views.generic import View,TemplateView,ListView,DetailView
from . import models

# Create your views here.
def index(request):
    return render(request, 'AppTwo/index.html')

def help(request):
    help_dict = {'help_insert': 'Help Page'}
    return render(request, 'AppTwo/help.html', context=help_dict)

# def users(request):
#     all_users = User.objects.all()
#     users_dict = {'user_list':all_users}
#     return render(request, 'AppTwo/users.html', context=users_dict)

def users(request):
    form = NewUserForm()

    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('Form invalid')

    return render(request, 'AppTwo/users.html',{'form':form})

class SchoolListView(ListView):
    model = models.School

class SchoolDetailView(DetailView):
    model = models.School
    template_name = 'AppTwo/school_detail.html'
