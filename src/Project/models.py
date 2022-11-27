from django.db import models
from django.contrib.auth.models import User
# DataFlair Models


class Category(models.Model):
    Name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.Name


class Item(models.Model):
    name = models.CharField(max_length=50)
    picture = models.ImageField(null=True, blank=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    discription = models.CharField(max_length=250, default="Available")
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


@property
def imageURL(self):
    try:
        url = self.image.url
    except:
        url = ''
    return url

# special order


class Customorder(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Delivered', 'Delivered'),
    )

    DELIVERY = (
        ('Pick Up', 'Pick Up'),
        ('Home Delivery', 'Home Delivery'),
    )

    status = models.CharField(max_length=50, null=True, choices=STATUS)
    name = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=150, null=True)
    address = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=100, null=True)
    delivery = models.CharField(max_length=50, null=True, choices=DELIVERY)
    description = models.CharField(max_length=300, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# supplier

class Supplier(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)



    def __str__(self):
        return self.name


class Product(models.Model):
    CATEGORY = (
        ('kilogram', 'kilogram'),
        (' liter', ' liter'),
    )

    name = models.CharField(max_length=200, null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    description = models.CharField(max_length=200, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Out for delivery', 'Out for delivery'),
        ('Delivered', 'Delivered'),
    )

    supplier = models.ForeignKey(
        Supplier, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    quantity = models.FloatField(null=True)
    total_price = models.FloatField(null=True)

    def __str__(self):
        return self.product.name


# cart function

class Customer(models.Model):
    # onetoone customer can have one user,user can have one customer
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, blank=True)
    # name as a string value
    name = models.CharField(max_length=200, null=True)
    # name as a string value
    email = models.CharField(max_length=200, null=True)
    password = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField()
    digital = models.BooleanField(default=False, null=True, blank=False)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
        return self._imageURL


class Order(models.Model):
    customer = models.ForeignKey(
        Customer, on_delete=models.SET_NULL, blank=True, null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.id)

    @property
    def shipping(self):
        shipping = False
        orderitems = self.orderitem_set.all()
        for i in orderitems:
            if i.product.digital == False:
                shipping = True
        return shipping

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total


class OrderItem(models.Model):  # single order can have many order items
    product = models.ForeignKey(
        Product, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(
        Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total


class DeliveryAddress(models.Model):
    customer = models.ForeignKey(
        Customer, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(
        Order, on_delete=models.SET_NULL, blank=True, null=True)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address


# Delivery

# Create your models here.
class RouteDetails(models.Model):
    dname = models.CharField(max_length=200, null=True)
    rname = models.CharField(max_length=200, null=True)
    km = models.IntegerField(null=True)
    town = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.rname


class Customer_order(models.Model):
    orderName = models.CharField(max_length=200, null=True)
    orderDate = models.DateField(max_length=200, null=True)
    Quantity = models.IntegerField(null=True)

    def __str__(self):
        return self.orderName


class Shop_order(models.Model):
    shopname = models.CharField(max_length=200, null=True)
    fitem = models.CharField(max_length=200, null=True)
    qty = models.IntegerField(null=True)

    def __str__(self):
        return self.shopname

# Employee


class Employee(models.Model):
    JOBTITLE = (
        ('Manager', 'Manager'),
        ('Cashier', 'Cashier'),
        ('Cook', 'Cook'),
        ('Helper', 'Helper'),
        ('Rider', 'Rider'),
    )

    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    ename = models.CharField(max_length=255, null=True)
    email = models.EmailField(max_length=254, null=True)
    address = models.CharField(max_length=100, null=True)
    contactnumber = models.IntegerField(null=True)
    gender = models.CharField(null=True, max_length=50, choices=GENDER)
    jobtitle = models.CharField(null=True, max_length=100, choices=JOBTITLE)
    basicsalary = models.FloatField(null=True, default=0)
    othours = models.FloatField(null=True, default=0)
    otrate = models.FloatField(null=True, default=0)
    allowances = models.FloatField(null=True, default=0)
    netsalary = models.FloatField(null=True, default=0)

    def __str__(self):
        return self.ename
