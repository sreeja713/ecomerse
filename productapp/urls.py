from django.urls import path
from . import views
urlpatterns = [
    path('addcategory', views.addcategory,name="addcategory"),
    path('show_category', views.show_category,name="show_category"),
    path('delete/<int:id>', views.delete,name="delete"),
    path('addproduct', views.addproduct,name="addproduct"),
    path('show_product', views.show_product,name="show_product"),
    path('productdelete/<int:id>', views.productdelete,name="productdelete"),
    path('add_to_cart/<int:id>', views.add_to_cart,name="add_to_cart"),
    path('cartpage', views.cartpage,name="cartpage"),
    path('cartdelete/<int:id>', views.cartdelete,name="cartdelete"),
    path('createorder', views.createorder,name="createorder"),
    path('orderpage', views.orderpage,name="orderpage"),
    path('orderdelete/<int:id>', views.orderdelete,name="orderdelete"),
]