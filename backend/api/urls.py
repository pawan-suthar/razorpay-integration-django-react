from django.urls import path
from .api_razorpay import CreateOrderApi


urlpatterns = [
    path("order/create/", CreateOrderApi.as_view(), name="createoderapi" )
    
]