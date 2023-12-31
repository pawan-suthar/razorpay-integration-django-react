from . import client
from rest_framework.serializers import ValidationError
from rest_framework import status


class RazorpayClient:
    def Create(self,amount,currency):
        data = {
            'amount':amount,
            'currency':currency
        }
        try:
            orderdata = client.order.create(data=data) 
            return orderdata   
        except Exception as e:
            raise ValidationError(
                {
                    "status_code":status.HTTP_400_BAD_REQUEST,
                    "message":str(e)
                }
            )