from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect

from django.contrib.auth.models import User

from login.forms import CreateUserForm
from login.models import customer_profile, product_info, order_info


# Create your views here.
def home(request):
    return render(request,'home.html')


def login_read(request):
    if request.method == 'POST':
        print("eeee")
        email = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        print(user)
        if user is not None:
            print(user)
            if user.is_superuser:
                print("22")
                login(request, user)
                return render(request,'adminnavbar.html')  # Redirect to admin page
            else:
                login(request, user)
                return render(request,'customernavbar.html')  # Redirect to user page
        else:
            messages.error(request, "Invalid username or password.")
    return redirect('loginpage')


def loginpage(request):
    return render(request,'login.html')


def profile(request):
    customer = customer_profile.objects.filter(client_id=request.user.id)
    return render(request,'customerprofile.html',{'customer':customer})


def addprofile(request):
    return render(request,'addprofile.html')


def submitinfo(request):
    if request.method == "POST":
        customer_info = customer_profile()
        customer_info.customer_first_name = request.POST.get('CustomerFName')
        customer_info.customer_last_name = request.POST.get('CustomerLName')
        customer_info.customer_email = request.POST.get('cemail')
        customer_info.customer_phone_number = request.POST.get('cnumber')
        customer_info.customer_address = request.POST.get('cadress')
        customer_info.client_id = request.user.id
        customer_info.save()
        return redirect('profile')
    return render(request,'addprofile.html')


def editprofile(request,id):
    modifyprofile = customer_profile.objects.filter(client_id=request.user.id, id=id)
    return render(request,'editprofile.html',{'modifyprofile':modifyprofile})


def deleteprofile(request,id):
    deleteprofile = customer_profile.objects.filter(client_id=request.user.id, id=id)
    deleteprofile.delete()
    return redirect('profile')


def updateprofile(request,id):
    update_profile = customer_profile.objects.filter(client_id=request.user.id, id=id)
    if request.method == 'POST':
        for j in update_profile:
            edit_info = customer_profile.objects.get(id=j.id)
            edit_info.customer_first_name = request.POST.get('reeventname')
            edit_info.customer_last_name = request.POST.get('reeventdesc')
            edit_info.customer_email = request.POST.get('reeventmessageheader')
            edit_info.customer_phone_number = request.POST.get('reeventbody')
            edit_info.customer_address = request.POST.get('reeventfooter')
            edit_info.save()
        return redirect('profile')
    return render(request,'editprofile.html',{'modifyprofile':update_profile})


def products(request):
    product_info_list = product_info.objects.filter(client_id=request.user.id)
    return render(request,'productlist.html',{'product_info_list':product_info_list})


def addproduct(request):
    return render(request,'addproduct.html')


def submitproduct(request):
    if request.method == 'POST':
        product_data = product_info()
        product_data.product_name = request.POST.get('ProductName')
        product_data.product_description = request.POST.get('Pdesc')
        product_data.product_price = request.POST.get('Price')
        product_data.product_id = request.POST.get('Pnumber')
        product_data.product_unit = request.POST.get('Punit')
        product_data.product_image = request.FILES['productimage']
        product_data.product_status = request.POST.get('productstatus')
        product_data.client_id = request.user.id
        product_data.save()
        return redirect('products')
    return render(request,'addproduct.html')


def editproduct(request,id):
    editproduct = product_info.objects.filter(client_id=request.user.id, id=id)
    return render(request,'editproduct.html',{'editproduct':editproduct})


def deleteproduct(request,id):
    deleteproduct = product_info.objects.filter(client_id=request.user.id, id=id)
    deleteproduct.delete()
    return redirect('products')


def updateproduct(request,id):
    updateproduct = product_info.objects.filter(client_id=request.user.id, id=id)
    if request.method == 'POST':
        for k in updateproduct:
            editupdateproduct = product_info.objects.get(id=k.id)
            editupdateproduct.product_name = request.POST.get('reproductname')
            editupdateproduct.product_description = request.POST.get('reproductdesc')
            editupdateproduct.product_price = request.POST.get('reprice')
            editupdateproduct.product_id = request.POST.get('reID')
            editupdateproduct.product_unit = request.POST.get('reunit')
            if 'reProductImage' in request.FILES and len(request.FILES['reProductImage']) != 0:
                editupdateproduct.product_image = request.FILES['reProductImage']
            else:
                editupdateproduct.product_image = k.product_image
            editupdateproduct.product_status = request.POST.get('restatus')
            editupdateproduct.save()
        return redirect('products')
    return render(request,'editproduct.html',{'editproduct':updateproduct})


def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        test_username = request.POST.get('username')
        test_email = request.POST.get('email')
        user_objects = User.objects.filter(username=test_username)
        user_objects1 = User.objects.filter(email=test_email.lower())
        if len(user_objects) == 0:
            if len(user_objects1) == 0:
                form = CreateUserForm(request.POST)
                if form.is_valid():
                    form.save()
                    user = form.cleaned_data.get('username')
                    messages.success(request, 'Account Was Created ' + user + ' ..!')
                    return redirect('loginpage')
                else:
                    context = {'form': form, 'invalid': 'text-danger', 'tex': "User name was already exist!"}
                    return render(request, 'signup.html', context)
            else:
                context = {'form': form, 'invalid': 'text-danger', 'tex': "Email name was already exist!"}
                return render(request, 'signup.html', context)
        else:
            context = {'form': form, 'invalid': 'text-danger', 'tex': "User name was already exist!"}
            return render(request, 'signup.html', context)
    else:
        context = {'form': form}
        return render(request, 'signup.html', context)


def customerhome(request):
    return render(request,'customerhome.html')


def buyfurniture(request):
    return render(request,'buyfurniture.html')


def catalogue(request):
    catalogue = product_info.objects.all()
    print(catalogue)
    return render(request,'catalogue.html',{'catalogue': catalogue})


def addtobuy(request,id):
    buyproduct = product_info.objects.filter(id=id)
    print(buyproduct)
    for b in buyproduct:
        saveorder = order_info()
        saveorder.product_name = b.product_name
        saveorder.product_description = b.product_description
        saveorder.product_price = b.product_price
        saveorder.product_id = b.product_id
        saveorder.product_unit = b.product_unit
        saveorder.product_image = b.product_image
        saveorder.order_status = 'a2c'
        saveorder.client_id = b.client_id
        saveorder.save()
    return render(request,'success.html')


def approveorder(request):
    customer_order_info = order_info.objects.filter(order_status='a2c')
    return render(request,'orderinfo.html',{'customer_order_info':customer_order_info})


def approveproduct(request,id):
    paidstatus = order_info.objects.filter(id=id)
    for j in paidstatus:
        j.order_status = "paid"
        j.save()
    return render(request,'info.html')


def cancelorder(request):
    return render(request,'cancelorder.html')