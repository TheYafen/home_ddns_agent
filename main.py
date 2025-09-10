import requests

def get_public_ip():
    try 
    ip = requests.get("https://api.myip.com").text
    return ip

a = 1
