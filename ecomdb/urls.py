from django.urls import path
from . import views


urlpatterns = [
    path('list',views.productList, name='List_products'),
    path('add',views.productAdd, name='Add_Product'),
    path('detail/<int:pk>', views.productDetail, name='Product_Details'),
    path('update/<int:pk>', views.productUpdate, name='Update_Product'),
    path('delete/<int:pk>', views.productDeleteChoose, name='Choose_Delete_Product'),
    path('deleted/<int:pk>', views.productDeleted, name='Product_deleted'),
    path('', views.home, name='Home_page'),
]