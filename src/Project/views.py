import os
from emp.decorators import allowed_users, unathenticated_user
from django.shortcuts import render, redirect
from django.utils.regex_helper import Group
from .models import Item, Category, Product, Supplier
from .models import Customorder
from .forms import ItemCreate, CreateUserForm, CustomorderForm
from django.http import HttpResponse
from .filters import CustomorderFilter,ProductFilter

from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required

from Project import forms

from .models import RouteDetails, Shop_order
from .forms import RouteDetalisForm
from .models import Customer_order
from .models import Shop_order
from .forms import CreateUserForm

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


from django.contrib.auth.models import Group


# DataFlair


def Food_Items(request):

    category = request.GET.get('category')
    if category == None:
        items = Item.objects.all()
    else:
        items = Item.objects.filter(category__Name=category)

    category = Category.objects.all()

    return render(request, 'FoodItem/items.html', {'category': category, 'items': items})


def index(request):
    category = request.GET.get('category')
    if category == None:
        items = Item.objects.all()
    else:
        items = Item.objects.filter(category__Name=category)

    category = Category.objects.all()

    return render(request, 'FoodItem/view.html', {'category': category, 'items': items})


def upload(request):
    upload = ItemCreate()
    if request.method == 'POST':
        upload = ItemCreate(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('index')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'index'}}">reload</a>""")
    else:
        return render(request, 'FoodItem/upload_form.html', {'upload_form': upload})


def update_FoodItem(request, Item_id):
    Item_id = int(Item_id)
    try:
        food_item = Item.objects.get(id=Item_id)
    except Item.DoesNotExist:
        return redirect('index')
    item_form = ItemCreate(request.POST or None, instance=food_item)
    if item_form.is_valid():
        item_form.save()
        return redirect('index')
    return render(request, 'FoodItem/update_form.html', {'update_form': item_form})


def delete_FoodItem(request, Item_id):
    product = Item.objects.get(id=Item_id)
    if len(product.picture) > 0:
        os.remove(product.picture.path)
        product.delete()
        return redirect('index')


def registerPage(request):

    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)

            return redirect('login')

    context = {'form': form}
    return render(request, 'FoodItem/register.html', context)


def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Username OR password is incorrect')

    context = {}
    return render(request, 'FoodItem/login.html', context)


def Home(request):
    context = {}
    return render(request, 'FoodItem/index.html', context)


def Contact(request):
    context = {}
    return render(request, 'FoodItem/contact.html', context)


def viewPhoto(request, pk):
    item = Item.objects.get(id=pk)
    return render(request, 'FoodItem/photo.html', {'item': item})


# main home page
def home(request):
    return render(request, 'custom_products/home.html')

# create special orders


def createCustomOrders(request):
    form = CustomorderForm()
    if request.method == 'POST':
        #print('Printing POST: ', request.POST)
        form = CustomorderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'custom_products/cusproducts.html', context)


# update special orders
def updateCustomOrders(request, pk):
    order = Customorder.objects.get(id=pk)
    form = CustomorderForm(instance=order)

    if request.method == 'POST':
        form = CustomorderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'custom_products/cusproducts.html', context)

# delete special orders


def deleteCustomOrders(request, pk):
    order = Customorder.objects.get(id=pk)
    if request.method == "POST":
        order.delete()
        return redirect('/')

    context = {'item': order}
    return render(request, 'custom_products/adminCustomOrderDelete.html', context)


# admin dashboard
def dashboard(request):
    return render(request, 'custom_products/dashboard.html')

# admin side special order list


def adminCustomOrders(request):
    cusorder = Customorder.objects.all()

    myFilter = CustomorderFilter(request.GET, queryset=cusorder)
    cusorder = myFilter.qs

    context = {'cusorder': cusorder, 'myFilter': myFilter}
    return render(request, 'custom_products/adminCustomOrders.html', context)


# supplier

# Delivery

def bakeryDelivery(request):
    return render(request, 'deliverysys/bakeryDelivery.html')


def choon(request):

    return render(request, 'deliverysys/choon.html')


def customerorder(request):

    customerorder = Customer_order.objects.all()

    return render(request, 'deliverysys/customerorder.html', {'customerorder': customerorder}
                  )


def shop(request):

    shop = Shop_order.objects.all()

    return render(request, 'deliverysys/shop.html', {'shop': shop})


def addroute(request):
    if request.method == "POST":
        form_route = RouteDetalisForm(request.POST or None)
        if form_route.is_valid():
            form_route.save()
            return redirect('rd')
        else:
            return render(request, 'deliverysys/addroute.html')
    else:
        return render(request, 'deliverysys/addroute.html')


def customerDetails(request):
    return render(request, 'deliverysys/customerDetails.html')


def editroute(request):

    if request.method == 'GET':
        id = request.GET['id']
        routedetail = RouteDetails.objects.get(pk=id)
        return render(request, 'deliverysys/editroute.html', {'routedetail': routedetail})

    if request.method == "POST":
        form_route = RouteDetalisForm(request.POST or None)
        id = request.POST['id']
        if form_route.is_valid():
            oldroutedetail = RouteDetails.objects.get(pk=id)
            oldroutedetail.dname = request.POST['dname']
            oldroutedetail.rname = request.POST['rname']
            oldroutedetail.km = request.POST['km']
            oldroutedetail.town = request.POST['town']
            oldroutedetail.save()
            return redirect('rd')
        else:
            routedetail = RouteDetails.objects.get(pk=id)
            return render(request, 'deliverysys/editroute.html', {'routedetail': routedetail})


def routeDelete(request):
    if request.method == "GET":
        id = request.GET['id']
        rdetail = RouteDetails.objects.get(pk=id)
        rdetail.delete()
        return redirect('rd')


def rd(request):

    rd = RouteDetails.objects.all()

    return render(request, 'deliverysys/rd.html', {'rd': rd})


def shopDetails(request):
    return render(request, 'deliverysys/shopDetails.html')


def specialFood(request):
    return render(request, 'deliverysys/specialFood.html')


def calculation(request):

    val1 = int(request.GET['nkm'])
    val2 = int(request.GET['amount'])

    result = val1 * val2

    return render(request, 'calculation.html', {'charge': result})


def salary(request):
    return render(request, 'salary.html')


def login(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:

                return redirect('home')
            else:
                messages.info(request, 'username OR password is incorrect')

        context = {}
        return render(request, 'login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


def registration(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                user = form.save()
                username = form.cleaned_data.get('username')

                group = Group.objects.get(name='customer')
                user.groups.add(group)

                messages.success(
                    request, 'Account was created for  ' + username)

                return redirect('login')

    context = {'form': form}
    return render(request, 'registration.html', context)


def user(request):
    return render(request, 'user.html')

# Employee


@unathenticated_user
def registerPage(request):
    form = CreateUserFrom()
    if request.method == 'POST':
        form = CreateUserFrom(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name='employee')
            user.groups.add(group)

            messages.success(request, 'Account was created for ' + username)

            return redirect('loginPage')

    context = {'form': form}
    return render(request, 'emp/register.html', context)


@unathenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('adminControls')
        else:
            messages.info(request, 'Username or password is incorrect')

    context = {}
    return render(request, 'emp/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('loginPage')


@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['admin'])
def addEmployee(request):
    form = addEmployeeform()
    if request.method == 'POST':
        #print('Printing POST:', request.POST)
        form = addEmployeeform(request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data.get('ename')
            messages.success(request, 'Record saved successfully for ' + name)

        return redirect('/viewEmployee')

    employee = {'form': form}
    return render(request, 'emp/addEmployee.html', employee)


@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['admin'])
def viewEmployee(request):
    employee = Employee.objects.all()

    myFilters = employeeFilter(request.GET, queryset=employee)
    employee = myFilters.qs

    context = {'employee': employee,
               'myFilters': myFilters}
    return render(request, 'emp/viewEmployee.html', context)


@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['admin'])
def updateEmployee(request, pk_test):

    employee = Employee.objects.get(id=pk_test)
    form = addEmployeeform(instance=employee)
    if request.method == 'POST':
        form = addEmployeeform(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('/viewEmployee')

    employee = {'form': form}
    return render(request, 'emp/addEmployee.html', employee)


@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['admin'])
def deleteEmployee(request, pk_test):
    employee = Employee.objects.get(id=pk_test)
    if request.method == 'POST':
        employee.delete()
        return redirect('/viewEmployee')

    context = {'i': employee}
    return render(request, 'emp/delete.html', context)


@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['admin'])
def salaryView(request):
    employee = Employee.objects.all()

    myFilters = employeeFilter(request.GET, queryset=employee)
    employee = myFilters.qs

    context = {'employee': employee, 'myFilters': myFilters}
    return render(request, 'emp/salaryView.html', context)


@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['admin'])
def salaryUpdate(request, pk_test):

    employee = Employee.objects.get(id=pk_test)
    form = addEmployeeform(instance=employee)
    if request.method == 'POST':
        form = addEmployeeform(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('/salaryView')

    employee = {'form': form}
    return render(request, 'emp/addEmployee.html', employee)


@login_required(login_url='loginPage')
@admin_only
def adminControls(request):
    return render(request, 'emp/adminControls.html')


@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['employee'])
def empSalaryView(request):
    emp = request.user.employee.name.all()
    print('EMPLOYEE', emp)
    context = {'emp': emp}

    return render(request, 'emp/empSalaryView.html', context)


#cart

def store(request):

	if request.user.is_authenticated:
		customer=request.user.customer
		order,created =Order.objects.get_or_create(customer=customer , complete=False)
		items = order.orderitem_set.all()
		cartItems =order.get_cart_items
	else:
		items =[]
		order ={'get_cart_total':0 , 'get_cart_items':0,'shipping':False}
		cartItems =order['get_cart_items']

		

	products=Product.objects.all()

	myFilter = ProductFilter(request.GET,queryset=products)
	products = myFilter.qs
	context ={'products':products,'cartItems':cartItems,'myFilter':myFilter}
	return render(request,'store/store.html',context)

def cart(request):

	if request.user.is_authenticated:
		customer=request.user.customer
		order,created =Order.objects.get_or_create(customer=customer , complete=False)
		items = order.orderitem_set.all()
		cartItems =order.get_cart_items
	else:
		items =[]
		order ={'get_cart_total':0 , 'get_cart_items':0,'shipping':False}
		cartItems = order['get_cart_items']

	context ={'items':items , 'order' :order,'cartItems':cartItems}
	return render(request,'store/cart.html',context)
	
def checkout(request):

	if request.user.is_authenticated:
		customer=request.user.customer
		order,created =Order.objects.get_or_create(customer=customer , complete=False)
		items = order.orderitem_set.all()
		cartItems =order.get_cart_items
	else:
		items =[]
		order ={'get_cart_total':0 , 'get_cart_items':0,'shipping':False}
		cartItems = order['get_cart_items']

	context ={'items':items , 'order' :order ,'cartItems':cartItems}
	
	
	return render(request,'store/checkout.html',context)
	
def updateItem(request):
	data = json.loads(request.body)
	productId = data['productId']
	action = data['action']

	print('Action:' , action)
	print('productId:' , productId)

	customer = request.user.customer
	product =Product.objects.get(id=productId)
	order,created =Order.objects.get_or_create(customer=customer , complete=False)

	orderItem, created =OrderItem.objects.get_or_create(order=order ,product =product)

	if action == 'add':
		orderItem.quantity = (orderItem.quantity + 1)
	elif action == 'remove':	 
		orderItem.quantity = (orderItem.quantity - 1)

	orderItem.save()

	if orderItem.quantity <= 0:
		orderItem.delete()
	return JsonResponse('Item was added' ,safe=False)

def processOrder(request):
	transaction_id=datetime.datetime.now().timestamp()
	data =json.loads(request.body)

	if request.user.is_authenticated:
		customer = request.user.customer
		order,created =Order.objects.get_or_create(customer=customer , complete=False)
		total = float(data['form']['total'])
		order.transaction_id = transaction_id

		if total == order.get_cart_total:
			order.complete =True
		order.save()

		if order.shipping == True:
			DeliveryAddress.objects.create(
			customer=customer,
			order=order,
			address=data['shipping']['address'],
			city=data['shipping']['city'],
			)

	else:
		print('User is not logged in...')
	return JsonResponse('payment complete' ,safe=False)


def export_to_csv(request):
	orderitems = OrderItem.objects.all()
	response =HttpResponse('text/csv')
	response['Content-Disposition'] = 'attachment ; filename =orderitem.csv'
	writer =csv.writer(response)
	writer.writerow(['product' ,'order','quantity','date_added'])
	orderitemfields =orderitems.values_list('product' ,'order','quantity','date_added')
	for orderitems in orderitemfields:
		writer.writerow(orderitems)
	return response
