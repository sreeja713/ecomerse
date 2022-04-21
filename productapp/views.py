
from multiprocessing.managers import SharedMemoryManager
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .forms import addCategoryForm,addProductForm
from django.contrib.auth.decorators import login_required, permission_required
from . models import Category,Product,Order
from .forms import OrderForm
# Create your views here.
from django.contrib.auth.models import Group
# create category
@permission_required('productapp.admin_permisions',raise_exception=True)
def addcategory(request):

    if request.method=="GET":
        form = addCategoryForm()
        return render(request,'addcategory.html',{'form':form})
    elif request.method=="POST":
        print("postfunction")
        form = addCategoryForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            print("sucess")
            return redirect('show_category')
        else:
            print("it is an ERROR")
            return redirect("addcategory")
#show Category
@permission_required('productapp.admin_permisions',raise_exception=True)
def show_category(request):
    category=Category.objects.all()
    return render(request,'show.html',{'category':category})

#delete category
@permission_required('productapp.admin_permisions',raise_exception=True)
def delete(request,id):
    category=Category.objects.get(id=id)
    category.image.delete(save=True)
    category.delete()
    return redirect('show_category')

#Product session started--------------------
@permission_required('productapp.admin_permisions',raise_exception=True)
def addproduct(request):
    if request.method=="GET":
        form = addProductForm()
        return render(request,'addproduct.html',{'form':form})
    elif request.method=="POST":
        form = addProductForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            
            return redirect('show_product')
        else:
            print("it is an ERROR")
            return redirect("addproduct")

#show product---
@permission_required('productapp.admin_permisions',raise_exception=True)
def show_product(request):
    product=Product.objects.all()
    return render(request,'show_product.html',{'product':product})

@permission_required('productapp.admin_permisions',raise_exception=True)
def productdelete(request,id):
    product=Product.objects.get(id=id)
    product.image.delete(save=True)
    product.delete()
    return redirect('show_product')

# @login_required(login_url='loginpage')
# def order(request,id):
#     if request.method=="GET":
#         order_details=Order.objects.get(id=id)
#         if order_details.status=="cart":

@login_required(login_url='loginpage')
def add_to_cart(request,id):
    if request.method=="GET":
        product_details=Product.objects.get(id=id)
        order_details = Order()
        order_details.user = request.user
        order_details.product = product_details
        order_details.Quantity=1
        order_details.address = 0
        order_details.price = product_details.price
        order_details.status = "Cart"
        order_details.save()
        return redirect("cartpage")
    else:
        return HttpResponse("it is POST")
        
@login_required(login_url='loginpage')
def cartpage(request):
    order_details = Order.objects.filter(status="Cart").select_related('user','product').all()
    total=0
    for price in order_details:
        total=total+price.price
    
    return render(request,"cart.html",{'order_details':order_details,'total':total})

def cartdelete(request,id):
    order=Order.objects.get(id=id)
    order.delete()
    return redirect('cartpage')


@login_required(login_url='loginpage')
def createorder(request):
    if request.method=="GET":
        order_details = Order.objects.filter(user=request.user,status="Cart").select_related('user','product').first()
        form=OrderForm()
        return render(request,'address.html',{'form':form})
    elif request.method=="POST":
        
        order_details = Order.objects.filter(user=request.user,status="Cart").select_related('user','product').first()
        print("\n",order_details.__dict__,"\n")
        form=OrderForm(request.POST)
        if form.is_valid():
            add={'house_name':form.cleaned_data['house_name'],'Area':form.cleaned_data['Area'],'pincode':form.cleaned_data['pincode'],'city':form.cleaned_data['city']}
            order_details.address=add
            order_details.status="Billing"
            order_details.save()
            return redirect('orderpage')
            
        else:
            return render(request,'address.html',{'form':form})

@login_required(login_url='loginpage')
def orderpage(request):
    full_order_list= Order.objects.filter(status="Billing").select_related('user','product').all()
    order_details = Order.objects.filter(user=request.user,status="Billing").select_related('user','product').all()

    order_details = Order.objects.filter(status="Billing")
    if not request.user.is_superuser:
        order_details = order_details.filter(user=request.user)
    order_details = order_details.select_related('user','product').all()

   
    return render(request,"order2.html",{'order_details':order_details,'full_order_list':full_order_list})
    
def orderdelete(request,id):
    order=Order.objects.get(id=id)
    order.delete()
    return redirect('orderpage')

   