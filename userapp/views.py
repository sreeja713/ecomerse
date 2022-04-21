
from multiprocessing import context
from unicodedata import category
from django.http import HttpResponse
from django.shortcuts import redirect, render
from . forms import SignUpForm,custom_loginform
from django.contrib.auth.models import Group
from django.contrib import messages

from django.contrib.auth import authenticate, logout,login
from django.contrib.auth.decorators import login_required
from productapp.models import Category,Product


# Create your views here.
def home(request):
    category=Category.objects.all()

    context={'category':category}
    return render(request,"home.html",context)
def signup(request):
    if request.method=="GET":
        form = SignUpForm()
        return render(request,"signup.html",{'form':form})
    else:
        form=SignUpForm(request.POST)
        if form.is_valid:
            user = form.save()
            if user:
                user.refresh_from_db() 
                user_group = Group.objects.get(name='User')
                user_group.user_set.add(user) 
                return redirect('loginpage')
            else:
                messages.error(
                    request, ('Something went wrong, Please try agian.'))
                return render(request, 'signup.html', {'form': form})
        else:
            form = SignUpForm()
            return render(request, 'signup.html', {'form': form})
        
def loginpage(request):
    if request.method=="GET":
        form=custom_loginform()
        form.fields['username'].widget.attrs['class'] = "form-control"
        form.fields['password'].widget.attrs['class'] = "form-control"
        return render(request,"login.html",{'form':form})
    elif request.method=="POST":
        form=custom_loginform(request.POST)
        
        if form.is_valid():
            print(form.cleaned_data)

            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")
            user=authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("home")
            else:
                messages.info(request,'invalid username or password')
                return redirect('loginpage')
        else:
            return redirect('loginpage')
    
@login_required(login_url='loginpage')
def logoutfunc(request):
    logout(request)
    print("\n logout\n")
    return redirect("home")

def usershow(request,id):
    product=Product.objects.filter(category=id).all()
    print(product)
    context={'product':product}
    return render(request,"usershow.html",context)

# def add_to_cart(request,id):
    # if request.method=="GET":
    #     from=cartForm:
    # return HttpResponse("hi")