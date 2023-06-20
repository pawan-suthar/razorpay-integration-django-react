from rest_framework.views import APIView
from rest_framework import status
from .serializer import CreateOrderSerializer
from rest_framework.response import Response
from backend.api.razorpay.main import RazorpayClient


rz_client = RazorpayClient



class CreateOrderApi(APIView):

    def post(self,request):
        create_order_serializer = CreateOrderSerializer(
            data = request.data
        )
        if create_order_serializer.isvalid():
            order_response = rz_client.Create(
                amount=create_order_serializer.validated_data.get("amount"),
                currency=create_order_serializer.validated_data.get("currency")
            )
            response = {
                "status_code":status.HTTP_201_CREATED,
                "message":"order created",
                "data":order_response
            }
            return Response(response, status=status.HTTP_201_CREATED)
        else:
            response = {
                "status_code":status.HTTP_400_BAD_REQUEST,
                "message":"bad request",
                "error":create_order_serializer.errors
            }
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
