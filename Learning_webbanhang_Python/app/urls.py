from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name="home"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('getImage/', views.getImage, name='getImage'),
    path('update_item/', views.updateItem, name='update_item'),
    path('bean/', views.BeanClass, name='bean'),
    path('bitter_ground/', views.BitterGourdClass, name='bitter_ground'),
    path('bottle_gourd/', views.BottleGourdClass, name='bottle_gourd'),
    path('broccoli/', views.BroccoliClass, name='broccoli'),
    path('cabbage/', views.CabbageClass, name='cabbage'),
    path('capsicum/', views.CapsicumClass, name='capsicum'),
    path('carrot/', views.CarrotClass, name='carrot'),
    path('cauliflower/', views.CauliflowerClass, name='cauliflower'),
    path('cucumber/', views.CucumberClass, name='cucumber'),
    path('papaya/', views.PapayaClass, name='papaya'),
    path('potato/', views.PotatoClass, name='potato'),
    path('pumpkin/', views.PumpkinClass, name='pumpkin'),
    path('radish/', views.RadishClass, name='radish'),
    path('tomato/', views.TomatoClass, name='tomato'),
    path('search_results/', views.search_results, name='search_results'),
    path('about_us/', views.About_us, name='about_us'),
    path('login/', views.Login, name='login'),
    path('register/', views.Register, name='register'),
]