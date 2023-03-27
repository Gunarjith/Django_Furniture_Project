from django.urls import path

from login import views

urlpatterns = [
    path('',views.home),
    path('loginpage/',views.loginpage,name='loginpage'),
    path('login/',views.login_read,name='login'),
    path('profile/',views.profile,name='profile'),
    path('addprofile/',views.addprofile,name='addprofile'),
    path('submitinfo/',views.submitinfo,name='submitinfo'),
    path('editprofile/<int:id>/',views.editprofile,name='editprofile'),
    path('deleteprofile/<int:id>/',views.deleteprofile,name='deleteprofile'),
    path('updateprofile/<int:id>/',views.updateprofile,name='updateprofile'),
    path('products/',views.products,name='products'),
    path('addproduct/',views.addproduct,name='addproduct'),
    path('submitproduct/',views.submitproduct,name='submitproduct'),
    path('editproduct/<int:id>/',views.editproduct,name='editproduct'),
    path('deleteproduct/<int:id>/',views.deleteproduct,name='deleteproduct'),
    path('updateproduct/<int:id>/',views.updateproduct,name='updateproduct'),
    path('register/',views.register,name='register'),
    path('customerhome/',views.customerhome,name='customerhome'),
    path('buyfurniture/',views.buyfurniture,name='buyfurniture'),
    path('catalogue/',views.catalogue,name='catalogue'),
    path('addtobuy/<int:id>/',views.addtobuy,name='addtobuy'),
    path('approveorder/',views.approveorder,name='approveorder'),
    path('approveproduct/<int:id>/',views.approveproduct,name='approveproduct'),
    path('cancelorder/',views.cancelorder,name='cancelorder')




]