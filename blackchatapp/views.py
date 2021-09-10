from django.shortcuts import render ,redirect , HttpResponse
from .forms import Create 
from .models import *
# Create your views here.
def index(request):
    return render(request,'index.html')

def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', context = {"products":products})
    
    

def payment(request):
    products = Product.objects.all()
    return render(request,'payment.html',context = {"products":products})





def register(request):
    form = Create(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('login')
    
    return render(request,'register.html',{'form':form})


    





