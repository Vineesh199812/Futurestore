from multiprocessing import context
from django.shortcuts import render,redirect

# Create your views here.

from django.views.generic import CreateView,TemplateView,FormView,DetailView,DeleteView,ListView
from django.contrib.auth import authenticate,login,logout
from Owner.models import Products,Carts
from Customer import forms
from django.urls import reverse_lazy

class RegistrationView(CreateView):
    form_class=forms.RegistrationForm
    template_name="registration.html"
    success_url=reverse_lazy("login")

class LoginView(FormView):
    template_name="login.html"
    form_class=forms.LoginForm

    def post(self,request,*args,**kw):   # we jst need **  it may be kw or kwargs or anything
        form=forms.LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")
            user=authenticate(request,username=username,password=password)
            if user:
                login(request,user)
                return redirect("home")
            else:
                return render(request,"login.html",{"form":form})

class HomeView(TemplateView):
    template_name="home.html"

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        all_products=Products.objects.all()
        context["products"]=all_products
        return context

class ProductDetailView(DetailView):
    template_name: str="product-detail.html"
    model=Products
    context_object_name="product"
    pk_url_kwarg = "id"

class AddtoCartView(DetailView):
    template_name = "addto-cart.html"
    form_class= forms.CartForm

    def get(self, request, *args, **kwargs):
        id=kwargs.get("id")
        product=Products.objects.get(id=id)
        return render(request,self.template_name,{"form":forms.CartForm(),"product":product})

    def post(self,request,*args,**kwargs):
        id=kwargs.get("id")
        product=Products.objects.get(id=id)
        qty=request.POST.get("qty")
        user=request.user
        Carts.objects.create(product)
        user=user,
        qty=qty
        return redirect("home")

class MyCartView(ListView):
    model=Carts
    template_name = "cart_list.html"
    context_object_name = "carts"

    def get_queryset(self):
        return Carts.objects.filter(user=self.request.user).exclude("cancelled")