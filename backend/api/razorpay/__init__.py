import razorpay
from django.conf import settings

client = razorpay.Client(auth=(settings.KEY_ID,settings.KEY_SECRET))