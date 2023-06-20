import razorpay
from django.conf import settings


client = razorpay.Client(auth=(
    settings.key_id,
    settings.key_secret
      ))