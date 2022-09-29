from multiprocessing import context
from django.shortcuts import render,redirect

# Create your views here.

from django.views.generic import CreateView,TemplateView,FormView,DetailView,DeleteView,ListView
from django.contrib.auth import authenticate,login,logout
from Owner.models import Products,Carts,Orders
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
                if request.user.is_superuser:
                    return redirect("dashboard")
                else:
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
    template_name="product-detail.html"
    model=Products
    context_object_name="product"
    pk_url_kwarg = "id"

class AddtoCartView(DetailView):
    template_name = "addto-cart.html"
    form_class = forms.CartForm

    def get(self, request, *args, **kwargs):
        id=kwargs.get("id")
        product=Products.objects.get(id=id)
        return render(request,self.template_name,{"form":forms.CartForm(),"product":product})

    def post(self,request,*args,**kwargs):
        id=kwargs.get("id")
        product=Products.objects.get(id=id)
        qty=request.POST.get("qty")
        user=request.user
        Carts.objects.create(product=product,
        user=user,
        qty=qty)
        return redirect("home")

class MyCartView(ListView):
    model=Carts
    template_name = "cart-list.html"
    context_object_name = "carts"

    def get_queryset(self):
        return Carts.objects.filter(user=self.request.user).exclude(status="cancelled").order_by("-created_date")   # - for sort in descendin order


class PlaceOrderView(FormView):
    template_name = "place-order.html"
    form_class = forms.OrderForm

    def post(self, request, *args, **kwargs):
        cart_id=kwargs.get("cid")
        product_id=kwargs.get("pid")
        cart=Carts.objects.get(id=cart_id)
        product=Products.objects.get(id=product_id)
        user=request.user
        delivery_address=request.POST.get("delivery_address")
        Orders.objects.create(product=product,
                              user=user,
                              delivery_address=delivery_address)
        cart.status="order-placed"
        cart.save()
        return redirect("home")


# def remove_product(request, *args, **kwargs):
#         id = kwargs.get("pk")
#         Carts.objects.get(id=id).delete()
#
#         # messages.success(request, "product has been removed from cart")
#         return redirect("home")
#
# class Checkout(DetailView):
#    model = Orders
#    template_name = "order.html"
#    form_class=forms.CheckoutForm


