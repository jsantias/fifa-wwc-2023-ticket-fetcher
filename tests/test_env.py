import os
from dotenv import load_dotenv

load_dotenv()

username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")
url = os.getenv("TARGET_URL")
hook_url = os.getenv("HOOK_URL")

print(username, password, url, hook_url)