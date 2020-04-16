from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from basicapp.forms import UserForm, UserProfileForm
from django.http import HttpResponseRedirect , HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.views.generic import TemplateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from basicapp.models import UserProfile
from django.db.models import Q
from django.contrib.auth.models import User



def index(request):
    return render(request,'basicapp/index.html')


def register(request):
    
    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            registered = True
            return render(request,'registration/scc_register.html')
        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    
    return render(request, 'registration/register.html/',
            {'user_form':user_form,
            'profile_form':profile_form,
            'registered':registered}) 

@login_required   
def detail_view(request,slug):
    user = get_object_or_404(User,username=request.user.username)
    user_data = UserProfile.objects.get(user=user)
    if (user_data.case == 'Reciver'):
        user_bloodType = donor_option[user_data.blood_type]
        user_profile = UserProfile.objects.filter(blood_type__in=user_bloodType, case__exact='Blood Donor')
    else:
        user_bloodType = reciver_option[user_data.blood_type]
        user_profile = UserProfile.objects.filter(blood_type__in=user_bloodType, case__exact='Reciver')
  
    context = {
        'user':user,
        'user_data':user_data,
        'user_profile':user_profile
    }
    return render(request,'basicapp/detail_view.html',context)

reciver_option = {
    'A+':['A+','AB+'],
    'A-':['A+','A-','AB+','AB-'],
    'B+':['B+', 'AB+'],
    'B-':['B+','B-','AB+','AB-'],
    'O+':['O+','A+','B+','AB+'],
    'O-':'all',
    'AB+':'AB+',
    'AB-':['AB+','AB-']
}

donor_option = {
    'A+':['A+','A-','O+','O-'],
    'A-':['A-','O-'],
    'B+':['B+', 'B-','O+','O-'],
    'B-':['B-','O-'],
    'O+':['O+','O-'],
    'O-':'O-',
    'AB+':'all',
    'AB-':['AB-','A-','B-','O-']  
}
    

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
        
            else:
                return HttpResponse('Account not active')
    
        else:
            print('Someone tried to login and failed!')
            return HttpResponse('invalid login details sipplied')
    else:
        return render(request,'registration/login.html',{})


def donation_method(request):
            return render(request, 'basicapp/donation_method.html')