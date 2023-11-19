from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseBadRequest
from django.http import JsonResponse
import json
from django import forms
from .models import *
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import numpy as np
import tensorflow as tf
from keras.models import load_model  # TensorFlow is required for Keras to work
import cv2  # Install opencv-python
import numpy as np
import os
import random
# Create your views here.
def home(request):
    if request.method == 'POST' and request.FILES['image']:
        image_file = request.FILES['image']
        fs = FileSystemStorage()
        filename = fs.save(image_file.name, image_file)
        image_path = os.path.join('app', 'static', 'images', filename)

        # Get the predicted class for the uploaded image '.' + uploaded_file_url
        predicted_class = predict_image(image_path)
        relative_path = image_path.replace('app\static\\', '')

        print("After replace - image_path:", image_path)
        print("After replace - relative_path:", relative_path)
        
        return render(request, 'app/home.html', {'uploaded_file_url': relative_path, 'predicted_class': predicted_class})

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete = False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}
        cartItems = order['get_cart_items']

    products = Product.objects.all()
    random_products = random.sample(list(products), min(len(products), 9))
    
    context = {
        'products': products,
        'random_products': random_products,
        'cartitems':cartItems
    }
    
    return render(request, 'app/home.html', context)

def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete = False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}
        cartItems = order['get_cart_items']
    context={'items':items, 
             'order':order,
             'cartitems':cartItems
             } # dùng chứa nội dung rỗng
    return render(request, 'app/cart.html', context)

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete = False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}
        cartItems = order['get_cart_items']
    context={'items':items, 
             'order':order,
             'cartitems':cartItems
             }
    return render(request, 'app/checkout.html', context)

def BeanClass(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete = False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}
        cartItems = order['get_cart_items']

    beans = Bean.objects.all()
    context={'beans':beans, 'cartitems':cartItems}
    return render(request, 'app/bean.html', context)

def BitterGourdClass(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete = False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}
        cartItems = order['get_cart_items']

    bitter_gourds = Bitter_Gourd.objects.all()
    context={'bitter_gourds':bitter_gourds,
             'cartitems':cartItems}
    return render(request, 'app/bitter_gourd.html', context)

def BottleGourdClass(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete = False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}
        cartItems = order['get_cart_items']

    bottle_gourds = Bottle_Gourd.objects.all()
    context={'bottle_gourds':bottle_gourds,
             'cartitems':cartItems}
    return render(request, 'app/bottle_gourd.html', context)

def BroccoliClass(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete = False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}
        cartItems = order['get_cart_items']

    broccolis = Broccoli.objects.all()
    context={'broccolis':broccolis, 'cartitems':cartItems}
    return render(request, 'app/broccoli.html', context)

def CabbageClass(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete = False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}
        cartItems = order['get_cart_items']

    cabbages = Cabbage.objects.all()
    context={'cabbages':cabbages, 'cartitems':cartItems}
    return render(request, 'app/cabbage.html', context)

def CapsicumClass(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete = False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}
        cartItems = order['get_cart_items']

    capsicums = Capsicum.objects.all()
    context={'capsicums':capsicums, 'cartitems':cartItems}
    return render(request, 'app/capsicum.html', context)

def CarrotClass(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete = False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}
        cartItems = order['get_cart_items']

    carrots = Carrot.objects.all()
    context={'carrots':carrots, 'cartitems':cartItems}
    return render(request, 'app/carrot.html', context)

def CauliflowerClass(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete = False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}
        cartItems = order['get_cart_items']

    cauliflowers = Cauliflower.objects.all()
    context={'cauliflowers':cauliflowers, 'cartitems':cartItems}
    return render(request, 'app/cauliflower.html', context)

def CucumberClass(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete = False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}
        cartItems = order['get_cart_items']

    cucumbers = Cucumber.objects.all()
    context={'cucumbers':cucumbers, 'cartitems':cartItems}
    return render(request, 'app/cucumber.html', context)

def PapayaClass(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete = False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}
        cartItems = order['get_cart_items']

    papayas = Papaya.objects.all()
    context={'papayas':papayas, 'cartitems':cartItems}
    return render(request, 'app/papaya.html', context)

def PotatoClass(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete = False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}
        cartItems = order['get_cart_items']
    
    potatoes = Potato.objects.all()
    context={'potatoes':potatoes, 'cartitems':cartItems}
    return render(request, 'app/potato.html', context)

def PumpkinClass(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete = False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}
        cartItems = order['get_cart_items']

    pumpkins = Pumpkin.objects.all()
    context={'pumpkins':pumpkins, 'cartitems':cartItems}
    return render(request, 'app/pumpkin.html', context)

def RadishClass(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete = False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}
        cartItems = order['get_cart_items']

    radishs = Radish.objects.all()
    context={'radishs':radishs, 'cartitems':cartItems}
    return render(request, 'app/radish.html', context)

def TomatoClass(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete = False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}
        cartItems = order['get_cart_items']

    tomatos = Tomato.objects.all()
    context={'tomatos':tomatos, 'cartitems':cartItems}
    return render(request, 'app/tomato.html', context)

def search_results(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete = False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}
        cartItems = order['get_cart_items']
    
    if request.method == 'GET':
        search_query = request.GET.get('q', '')

        # Thực hiện tìm kiếm trong cơ sở dữ liệu
        bean_results = Bean.objects.filter(name__icontains=search_query)
        bitter_gourd_results = Bitter_Gourd.objects.filter(name__icontains=search_query)
        bottle_gourd_results = Bottle_Gourd.objects.filter(name__icontains=search_query)
        broccoli_results = Broccoli.objects.filter(name__icontains=search_query)
        cabbage_results = Cabbage.objects.filter(name__icontains=search_query)
        capsicum_results = Capsicum.objects.filter(name__icontains=search_query)
        carrot_results = Carrot.objects.filter(name__icontains=search_query)
        cauliflower_results = Cauliflower.objects.filter(name__icontains=search_query)
        cucumber_results = Cucumber.objects.filter(name__icontains=search_query)
        papaya_results = Papaya.objects.filter(name__icontains=search_query)
        potato_results = Potato.objects.filter(name__icontains=search_query)
        pumpkin_results = Pumpkin.objects.filter(name__icontains=search_query)
        radish_results = Radish.objects.filter(name__icontains=search_query)
        tomato_results = Tomato.objects.filter(name__icontains=search_query)

        # Kết hợp kết quả từ cả hai bảng
        productSelected = list(bean_results) + list(bitter_gourd_results) + list(bottle_gourd_results) + \
        list(broccoli_results) + list(cabbage_results) + list(capsicum_results) + list(carrot_results) + \
        list(cauliflower_results) + list(cucumber_results) + list(papaya_results) + list(potato_results) + \
        list(pumpkin_results) + list(radish_results) + list(tomato_results)

        context = {
            'search_query': search_query,
            'productSelected': productSelected,
            'cartitems':cartItems
        }

        return render(request, 'app/search_results.html', context)

    return render(request, 'app/search_results.html')

def getImage(request):
    if request.method == 'POST' and request.FILES.get('image'):
        # Get the uploaded image from the request
        image = request.FILES['image']

        # Define the destination path where the image will be saved
        destination_path = os.path.join(settings.MEDIA_ROOT, 'imagesUser', image.name)

        # Check if the directory exists, if not, create it
        os.makedirs(os.path.dirname(destination_path), exist_ok=True)

        try:
            # Save the image to the destination path
            with open(destination_path, 'wb') as f:
                for chunk in image.chunks():
                    f.write(chunk)
                
            return HttpResponse('Image uploaded successfully')
        
        except Exception as e:
            return HttpResponseBadRequest('Error uploading image: {}'.format(str(e)))

    return HttpResponseBadRequest('Invalid request')

# Disable scientific notation for clarity
np.set_printoptions(suppress=True)
relative_path = 'templates\model\keras_model.h5'

templates_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'app')

absolute_path = os.path.join(templates_dir, relative_path)
# Load the model
model = load_model(absolute_path, compile=True)

# Load the labels
class_names = ["Đậu Hà Lan", "Khổ qua", "Bầu", "Cà tím", "Bông cải xanh", "Bắp cải", "Ớt chuông", "Cà rốt", "Súp lơ", "Dưa chuột", "Đu đủ", "Khoai tây", "Bí ngô", "Củ cải trắng", "Cà chua"]

def predict_image(image_path):
    # Load and preprocess the image
    img = tf.keras.preprocessing.image.load_img(image_path, target_size=(224, 224))
    img_array = np.asarray(img, dtype=np.float32).reshape(1, 224, 224, 3)
    img_array = (img_array / 127.5) - 1
    #img_array = preprocess_input(img_array)

    # Make predictions
    prediction = model.predict(img_array)
    index = np.argmax(prediction)
    class_name = class_names[index]

    return class_name 

def About_us(request):
    return render(request, 'app/AboutUs_Page.html')

def Login(request):
    return render(request, 'app/Login.html')

def Register(request):
    return render(request, 'app/Register.html')

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete = False)
    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)
    if action == 'add':
        orderItem.quantity = orderItem.quantity + 1
    elif action == 'remove':
        orderItem.quantity = orderItem.quantity - 1
    orderItem.save()
    if orderItem.quantity <= 0:
        orderItem.delete()
    
    return JsonResponse('Item was added', safe=False)