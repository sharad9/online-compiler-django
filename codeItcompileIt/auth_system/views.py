from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required
def HomePage(request):
    return render(request, 'auth_system/index.html', {})

def Register(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('sname')
        name = request.POST.get('uname')
        email = request.POST.get('email')
        password = request.POST.get('pass')

        new_user = User.objects.create_user(name, email, password)
        new_user.first_name = fname
        new_user.last_name = lname
        new_user.save()
        return redirect('login-page')
  
    return render(request, 'auth_system/register.html', {})

def Login(request):
    
    if request.method == 'POST':
        name = request.POST.get('uname')
        password = request.POST.get('pass')

        user = authenticate(request, username=name, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect("http://localhost:3000/")
        else:
            return render(request, 'auth_system/login.html', {'error':'Wrong credentials !'})

    return render(request, 'auth_system/login.html', {})

def logoutuser(request):
    logout(request)
    return redirect('login-page')

def welcome(request):
    return render(request, 'auth_system/welcome.html', {})


'''
const validatePassword =(p)=> {
    const errors = [];
    var specials = /[^A-Za-z 0-9]/g;

    if (specials.test(p)) {
      errors.push("Your class name should only contain Letters And Digits.");
    } else
      if (p[0].search(/[A-Z]/) < 0) {
        errors.push("Your class name must start with one upper case letter.");
      } else

        if (p.length < 1) {
          errors.push("Your class name must be at least 1 characters");
        } else
          if (p.length > 32) {
            errors.push("Your class name must be at max 32 characters");
          } 

    if (errors.length > 0) {
      document.getElementById('userNameStatus').innerText = errors[0];
      errors.shift();
      console.log(errors.join("\n"));
      return false;
    }
    document.getElementById('userNameStatus').innerText = "You Are Ready To Proceed.";
    return true;
  }
'''