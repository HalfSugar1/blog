from django.shortcuts import render,redirect
from django.contrib.auth import authenticate , login , logout
from django.http import HttpResponse
from .forms import UserLoginForm , UserRegisterForm , ProfileForm
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def user_login(request):
    if request.method == 'POST':
        user_login_form = UserLoginForm(data=request.POST)
        if user_login_form.is_valid():
            data = user_login_form.cleaned_data
            user = authenticate(username=data['username'],password=data['password'])
            if user:
                login(request,user)
                return redirect('Article_List')
            else:
                return HttpResponse('账号或密码输入有误，请重新输入~')
    elif request.method == 'GET':
        user_login_form = UserLoginForm()
        context = {'form':user_login_form}
        return render(request,'control/login.html',context)
    else:
        return HttpResponse('请用GET或者POST请求数据')

def user_logout(request):
    logout(request)
    return redirect('Article_List')

def user_register(request):
    if request.method == 'POST':
        user_register_form = UserRegisterForm(data=request.POST)
        if user_register_form.is_valid():
            new_user = user_register_form.save(commit=False)
            new_user.set_password(user_register_form.cleaned_data['password'])
            new_user.save()
            login(request,new_user)
            return redirect('Article_List')
        else:
            return HttpResponse('注册表单输入有误，请重新输入')
    elif request.method == 'GET':
        user_register_form = UserRegisterForm()
        context = {'form': user_register_form, }
        return render(request,'control/register.html',context)
    else:
        return HttpResponse('请用GET或POST请求数据')

@login_required(login_url='/control/login/')
def user_delete(request, id ):
    if request.method == 'POST':
        user = User.objects.get(id=id)
        if request.user == user:
            logout(request)
            user.delete()
            return redirect('Article_List')
        else:
            return HttpResponse('你没有删除操作')
    else:
        return HttpResponse('仅接受post请求')

@login_required(login_url='/control/login/')
def profile_edit(request,id):
    user = User.objects.get(id=id)
    if Profile.objects.filter(user_id=id).exists():
        profile = Profile.objects.get(user_id=id)
    else:
        profile = Profile.objects.create.create(user=user)

    if request.method == 'POST':
        if request.user != user:
            return HttpResponse('你没有权限修改此用户信息')
        profile_form = ProfileForm(request.POST,request.FILES)
        if profile_form.is_valid():
            profile_cd = profile_form.cleaned_data
            profile.phone = profile_cd['phone']
            profile.bio = profile_cd['bio']
            if 'avatar' in request.FILES:
                profile.avatar = profile_cd['avatar']
            profile.save()
            return redirect('control:profile_edit',id=id)
        else:
            return HttpResponse('注册表单输入有误，请重新输入~')

    elif request.method == 'GET':
        profile_form = ProfileForm()
        context = {'profile_form':profile_form,'profile':profile,'user':user}
        return render(request,'control/edit.html',context)
    else:
        return HttpResponse('情使用GET或POST请求数据')
