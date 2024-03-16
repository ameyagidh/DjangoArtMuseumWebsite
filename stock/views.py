from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import authenticate, login,logout
from .forms import *
# from .forms import ContactUsForm,CustomerSignUpForm,ArtistSignUpForm,CustomerForm,ArtistForm,Artform
from django.contrib.auth.decorators import login_required
from collections import Counter
from django.urls import reverse
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib import auth

from .models import Customer,Artist,Art,Order
# Create your views here.

def index_view(request):
    query 	= request.GET.get('q')
    if query:
        var=Art.objects.filter(Q(category=query)).distinct()
        return render(request,'base.html',{'var':var})
    var = Art.objects.all()
    background=True
    return render(request,'base.html',{'var':var,'background':background})

def logouts(request):
    print('logged out')
    logout(request)

    return redirect('index')

#Customer site

def login_customer_request(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        user     = authenticate(username=username,password=password)
        if user is not None:
            if user.is_active:
                if(user.is_customer == False):
                    return render(request, 'SignCustomer.html', {'error_message': 'Your account not registered as Customer'})

                login(request,user)
                return redirect("index")
            else:
                return render(request,'SignCustomer.html',{'error_message':'Your account disable'})
        else:
            return render(request,'SignCustomer.html',{'error_message': 'Invalid Login'})
    return render(request,'SignCustomer.html')
    



def sign_up_customer_request(request):
    form =CustomerSignUpForm(request.POST or None)
    if form.is_valid():
        user      = form.save(commit=False)
        username  = form.cleaned_data['username']
        password  = form.cleaned_data['password']

        user.is_customer=True
        user.set_password(password)
        user.save()
        user = authenticate(username=username,password=password)
        if user is not None:
            if user.is_active:
                login(request,user)
                return redirect("cprofile")
    
    context ={
        'form':form
    }
    return render(request,'SignCustomer.html',context)

#Create customer profile 
def createCustomer(request):
    form = CustomerForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        return redirect("profile")
    context={
    'form':form,
    'title':"PERSONAL DETAILS"
    }
    return render(request,'profileform.html',context)


def customerProfile(request ,pk=None):
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user=request.user  
    return render(request,'profile.html',{'user':user})



#  Update customer detail
def updateCustomer(request,id):
    form    = CustomerForm(request.POST or None,instance=request.user.customer)
    if form.is_valid():
        form.save()
        return redirect('profile')
    context={
    'form':form,
    'title':"Update Your profile"
    }
    return render(request,'profileform.html',context)

# Contact US view
def ContactUs_view(request):
    form = ContactUsForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("index")
     
    return render(request,'Contact.html',{})

#Artist Site
def login_artist_request(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        user     = authenticate(username=username,password=password)
        if user is not None:
            if user.is_active:
                if(user.is_artist == False):
                    return render(request,'SignArtist.html',{'error_message':'Your not registered as Artist '})

                login(request,user)
                return redirect("aprofile")
            else:
                return render(request,'SignArtist.html',{'error_message':'Your account disable'})
        else:
            return render(request,'SignArtist.html',{'error_message': 'Invalid Login'})
    return render(request,'SignArtist.html')

def sign_up_artist_request(request):
    form = ArtistSignUpForm(request.POST or None)
    if form.is_valid():
        user      = form.save(commit=False)
        username  = form.cleaned_data['username']
        password  = form.cleaned_data['password']
        user.is_artist=True
        user.set_password(password)
        user.save()
        user = authenticate(username=username,password=password)
        if user is not None:
            if user.is_active:
                login(request,user)
                return redirect("acreate")
    context ={
        'form':form
    }
    return render(request,'SignArtist.html',context)

def artistProfile(request,pk=None):
	if pk:
		user = User.objects.get(pk=pk)
	else:
		user=request.user
	
	return render(request,'artistprofile.html',{'user':user})

# create Artist detail
# @login_required(login_url='/login/artist/')
def createartist(request):
	form=ArtistForm(request.POST or None,request.FILES or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.user = request.user
		instance.save()
		return redirect("aprofile")
	context={
	'form':form,
	'title':"Complete Your Artist Profile"
	}
	return render(request,'artist_profile_form.html',context)

#Update Artist detail
# @login_required(login_url='/login/artist/')
def updateartist(request,id):
	form  	 = ArtistForm(request.POST or None,request.FILES or None,instance=request.user.artist)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.user = request.user
		instance.save()
		return redirect("aprofile")
	context={
	'form':form,
	'title':"Update Your Artist profile"
	}
	return render(request,'artist_profile_form.html',context)

def Add_Art_view(request):
    if not request.user.is_authenticated:
        return redirect("login_artist")

    Ar_id=Artist.objects.filter(id=request.user.artist.id)
    print(Ar_id[0])
    if request.POST:
        newart = Art()
        newart.Artist_id=Ar_id[0]
        newart.category=str(request.POST['category'])
        newart.name=str(request.POST['name'])
        newart.descrip=str(request.POST['descrip'])
        newart.price=int(request.POST['price'])
        newart.image= (request.FILES['image'])
        newart.quantity=int(request.POST['quantity'])
        newart.save()
        return redirect("aprofile")
    context={
    'title':"Add Your Art"
    }
    return render(request,'artform.html',context)


def Art_view(request,Art_id):
	view = Art.objects.get(Art_id=Art_id)
	addcart = request.GET.get('addtocart')
	if addcart:
		redirect('Cart')
	return render(request,'Art.html',{'view':view})


def add_to_cart(request, Art_id):
    if (request.user.is_customer == False):
        return render(request, 'SignCustomer.html', {'error_message': 'Your account not registered as Customer'})

    Ar=Art.objects.filter(Art_id=Art_id)
    custo=Customer.objects.filter(id=request.user.customer.id)
    
    cusAdd = custo[0].address
    cus=custo[0]
    prev_addcart=Order.objects.filter(Art_id=Ar[0]).filter(orderedBy=cus)

    my_cart = Order()
    if not prev_addcart:
        my_cart.Art_id = Ar[0]
        my_cart.orderedBy = cus
        my_cart.total_amount = Ar[0].price
        my_cart.delivery_addr = cusAdd
        my_cart.save()

    total=0
    count=0
    items=[]

    mycart= Order.objects.filter(orderedBy=cus)
    
    for item in mycart:
        temp=[]
        Ar=Art.objects.filter(name=item.Art_id)
        temp.append(Ar[0].Artist_id)
        temp.append(Ar[0].Art_id)
        temp.append(item.quantity)
        temp.append(Ar[0].name)
        temp.append(Ar[0].descrip)
        temp.append(Ar[0].price)
        temp.append(Ar[0].image)
        items.append(temp)

        total=total+item.total_amount
        count=count+1
    
    context={
        'items':items,
        'total':total,
        'count':count,
    }
    return render(request,'cart.html',context)

def MyCart_view(request):
    if (request.user.is_customer == False):
        return render(request, 'SignCustomer.html', {'error_message': 'Your account not registered as Customer'})

    custo=Customer.objects.filter(id=request.user.customer.id)
    
    cusAdd = custo[0].address
    cus=custo[0]

    total=0
    count=0
    items=[]

    mycart= Order.objects.filter(orderedBy=cus)
    
    for item in mycart:
        temp=[]
        Ar=Art.objects.filter(name=item.Art_id)
        temp.append(Ar[0].Artist_id)
        temp.append(Ar[0].Art_id)
        temp.append(item.quantity)
        temp.append(Ar[0].name)
        temp.append(Ar[0].descrip)
        temp.append(Ar[0].price)
        temp.append(Ar[0].image)
        items.append(temp)

        total=total+item.total_amount
        count=count+1
    
    context={
        'items':items,
        'total':total,
        'count':count,
    }
    return render(request,'cart.html',context)


def payment_view(request):
    if (request.user.is_customer == False):
        return render(request, 'SignCustomer.html', {'error_message': 'Your account not registered as Customer'})

    custo=Customer.objects.filter(id=request.user.customer.id)
    
    cusAdd = custo[0].address
    cus=custo[0]

    total=0
    count=0
    items=[]

    mycart= Order.objects.filter(orderedBy=cus)
    
    for item in mycart:
        temp=[]
        Ar=Art.objects.filter(name=item.Art_id)
        temp.append(Ar[0].Artist_id)
        temp.append(Ar[0].Art_id)
        temp.append(item.quantity)
        temp.append(Ar[0].name)
        temp.append(Ar[0].descrip)
        temp.append(Ar[0].price)
        temp.append(Ar[0].image)
        items.append(temp)

        total=total+item.total_amount
        count=count+1
    
    context={
        'items':items,
        'total':total,
        'count':count,
    }
    return render(request,'Payment.html',context)


