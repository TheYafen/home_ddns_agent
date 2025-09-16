import requests

def get_public_ip():
    try:
        ##Another API: https://api.myip.com
        ip = requests.get("https://api.ipify.org", timeout=5).text
    except Exception as e:
        print(f"Error getting IP: {e}")
        return None
    return ip



a = 1
