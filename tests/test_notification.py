from slack_client import send_notification
import os
from dotenv import load_dotenv

load_dotenv()

hook_url = os.getenv("HOOK_URL")
message="Hello World!"

send_notification(hook_url=hook_url, message=message)

# from dotenv import load_dotenv
# import os

# load_dotenv()

# my_password = os.getenv("Password")
# print(f"Password:{my_password}")