from django.shortcuts import render
from . forms import UserForm,UserProfileInfoForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required


def home(request):
    return render (request,'accounts/home.html')


def about(request):
    return render (request,'accounts/about.html')


def register(request):

    registered=False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form=UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user=user_form.save()
            user.set_password(user.password)
            user.save()

            profile=profile_form.save(commit=False)
            profile.user=user

            if 'profile_pic' in request.FILES:
                profile.profile_pic=request.FILES['profile_pic']

            profile.save()

            registered=True

        else:
            print(user_form.errors,profile_form.errors)


        if registered:
            return HttpResponseRedirect(reverse('user_login'))


    else:

        user_form=UserForm()
        profile_form=UserProfileInfoForm()


    return render(request,'accounts/register.html',{'user_form':user_form, 'profile_form':profile_form, 'registered':registered})



def user_login(request):


    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(username=username,password=password)


        if user:
            if user.is_active:
                login(request,user)
                request.session['user_id']=user.profile.pk

                return HttpResponseRedirect(reverse('predict:predict', kwargs={'pk': user.profile.pk}))

            else:
                return HttpResponse('Account not active')

        else:
            print('Tried login and failed')
            print('username:{} and password:{}'.format(username,password))
            return HttpResponse('Invalid login ')


    else:
        return render(request,'accounts/login.html',{})


@login_required
def user_logout(request):
    #del request.session['user_id']
    request.session.flush()
    logout(request)
    return HttpResponseRedirect(reverse('home'))