URL = "https://reservations.arestravel.com/hotel/list/content/20442/m1554?Search%5BhotelRegion%5D=m1554&Search%5BcheckInDate%5D=01/22/2025&Search%5BcheckOutDate%5D=01/26/2025&Search%5BroomOccupancies%5D%5B0%5D%5BnumberOfAdults%5D=1&Search%5BroomOccupancies%5D%5B0%5D%5BnumberOfChildren%5D=0&Search%5BkeywordSearch%5D=&Search%5Bsort%5D=&Search%5BstarRating%5D=&Search%5BlowPrice%5D=&Search%5BhighPrice%5D=&Search%5Bsearch%5D=&customNavLink=0&Search%5Bnear%5D=&Search%5Blatitude%5D=&Search%5Blongitude%5D=&Search%5BlocationSearch%5D=National%20Harbor%20/%20Oxon%20Hill,%20Washington,%20DC&Search%5BpoiDistance%5D="

import requests
from dotenv import load_dotenv
import os
from models import Model

load_dotenv()

response = requests.get(URL)
model = Model.parse_obj(response.json())

def is_hotel_sold_out(hotel_name: str) -> bool:
    for hotel in model.hotels:
        if hotel.name == hotel_name:
            return hotel.soldOutMessage
    return False

def send_sms_notification(message: str):
    from twilio.rest import Client
    client = Client(os.getenv("TWILIO_SID"), os.getenv("TWILIO_AUTH_TOKEN"))
    try:
        message = client.messages.create(
            body=message,
            to=os.getenv("RECEIVER_PHONE_NUMBER"),
            from_=os.getenv("TWILIO_PHONE_NUMBER")
        )
        print(f"SMS sent to {os.getenv('RECEIVER_PHONE_NUMBER')} with SID: {message.sid}")
    except Exception as e:
        print(f"Failed to send SMS: {e}")

def send_email_notification(subject: str, message: str):
    return requests.post(
        f"https://api.mailgun.net/v3/{os.getenv("MAILGUN_DOMAIN")}/messages",
        auth=("api", os.getenv("MAILGUN_API_KEY")),
        data={
            "from": os.getenv("MAILGUN_SENDER_EMAIL"),
            "to": os.getenv("MAILGUN_RECEIVER_EMAIL"),
            "subject": subject,
            "text": message,
        }
    )


desired_hotes = [
    "Gaylord National Resort & Convention Center"
]

if __name__ == "__main__":
    for hotel in desired_hotes:
        if is_hotel_sold_out(hotel):
            pass
            #send_sms_notification(f"{hotel} is sold out")
            #send_email_notification("Hotel Sold Out", f"{hotel} is sold out")
        else:
            #send_sms_notification(f"{hotel} is available")
            send_email_notification("Hotel Available", f"{hotel} is available")