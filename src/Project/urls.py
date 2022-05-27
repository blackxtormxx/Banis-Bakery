from django.urls import path
from . import views
from List.settings import DEBUG, STATIC_URL, STATIC_ROOT, MEDIA_URL, MEDIA_ROOT
from django.conf.urls.static import static
urlpatterns = [

    path('home/', views.Home, name="home"),
    path('', views.index, name='index'),
    path('items/', views.Food_Items, name='view'),
    path('upload/', views.upload, name='upload-Item'),
    path('update/<str:Item_id>', views.update_FoodItem),
    path('delete/<str:Item_id>', views.delete_FoodItem),

    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('photo/<str:pk>/', views.viewPhoto, name='photo'),
    path('contact/', views.Contact, name="contact"),

    path('dashboard/', views.dashboard, name="admin_dashboard"),
    path('adminCustomOrders/', views.adminCustomOrders, name="special_orders"),
    path('cusproducts/', views.createCustomOrders, name="create_CustomOrder"),
    path('update_adminCustomOrders/<str:pk>/',
         views.updateCustomOrders, name="update_CustomOrder"),
    path('delete_adminCustomOrders/<str:pk>/',
         views.deleteCustomOrders, name="delete_CustomOrder"),

    # Delivery



    path('choon/', views.choon, name='choon'),
    path('customerorder/', views.customerorder, name='customerorder'),
    path('shop/', views.shop, name='shop'),
    path('addroute/', views.addroute, name='addroute'),
    path('customerDetails/', views.customerDetails, name='customerDetails'),
    path('editroute/', views.editroute, name='editroute'),
    path('delete/', views.routeDelete, name='deleteroute'),
    path('rd/', views.rd, name='rd'),
    path('shopDetails/', views.shopDetails, name='shopDetails'),
    path('specialFood/', views.specialFood, name='specialFood'),
    path('calculation', views.calculation, name='calculation'),
    path('salary', views.salary, name='salary'),

    # cart
    path('cart/',views.cart,name="cart"),
    path('checkout/',views.checkout,name="checkout"),
    path('update_item/',views.updateItem,name="update_item"),
    path('login/',views.loginpage,name="login"),
    path('register/',views.register,name="register"),
    path('process_order/', views.processOrder, name="process_order"),

    # supplier
    # path('logout/', views.logoutUser, name="logout"),
    # path('user/', views.userPage, name="user-page"),
    # path('supdashb/', views.supdashb, name="supdashb"),
    # path('products/', views.products, name='products'),
    # path('supplier/<str:pk_test>/', views.supplier, name="supplier"),

    # path('create_order/', views.createOrder, name="create_order"),
    # path('update_order/<str:pk>/', views.updateOrder, name="update_order"),
    # path('delete_order/<str:pk>/', views.deleteOrder, name="delete_order"),
    # path('export-to-csv', views.export_to_csv, name="export-to-csv")



    # Employee
    path('addEmployee/', views.addEmployee, name="addEmployee"),
    path('viewEmployee/', views.viewEmployee, name="viewEmployee"),
    path('updateEmployee/<str:pk_test>/',
         views.updateEmployee, name="updateEmployee"),
    path('deleteEmployee/<str:pk_test>/',
         views.deleteEmployee, name="deleteEmployee"),
    path('salaryView/', views.salaryView, name="salaryView"),
    path('salaryUpdate/<str:pk_test>/',
         views.salaryUpdate, name="salaryUpdate"),
    path('adminControls/', views.adminControls, name="adminControls"),
    path('empSalaryView/', views.empSalaryView, name="empSalaryView"),



]
# DataFlair
if DEBUG:
    urlpatterns += static(STATIC_URL, document_root=STATIC_ROOT)
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
