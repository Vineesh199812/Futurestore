from django.shortcuts import render,redirect

# Create your views here.

from django.views.generic import TemplateView,ListView,DetailView
from django.contrib import messages
from Owner.models import Orders
from django.core.mail import send_mail
from Owner.forms import OrderUpdateForm

class AdminDashBoardView(TemplateView):
    template_name = "dashboard.html"

    def form_valid(self, form):
        messages.success(self.request,"you are logged in..")
        return super().form_valid(form)


    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)    # to override parent
        cnt=Orders.objects.filter(status="order-placed").count()
        context["count"]=cnt
        return context

class OrdersListView(ListView):
    model=Orders
    context_object_name = "orders"
    template_name = "owner/admin_listorder.html"

    def get_queryset(self):
        return Orders.objects.filter(status="order-placed")


class OrderDetailView(DetailView):
    model = Orders
    template_name = "owner/order-details.html"
    pk_url_kwarg = "id"
    context_object_name = "order"

    def get_context_data(self, **kwargs):
        context=super().get_context_data()
        form=OrderUpdateForm()
        context["form"]=form
        return context

    def post(self,request,*args,**kw):
        order=self.get_object()
        print(self.get_object())
        form=OrderUpdateForm(request.POST)
        if form.is_valid():
            order.status=form.cleaned_data.get("status")
            order.expected_delivery_date=form.cleaned_data.get("expected_delivery_date")
            dt=form.cleaned_data.get("expected_delivery_date")
            order.save()
            send_mail(
                "order delivery update future store",
                f"your order will be delivered on {dt}",
                "vineeshm199812@gmail.com",
                ["vineeshm199811@gmail.com"]
            )
            print(form.cleaned_data)
            return redirect("dashboard")