from django.shortcuts import render, redirect
import requests
from django.http import HttpResponseRedirect
import json
# Create your views here.

def base64_encode(message):
    import base64
    message_bytes = message.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')
    return base64_message



def zoom_callback(request):
    code = request.GET["code"]
    data = requests.post(f"https://zoom.us/oauth/token?grant_type=authorization_code&code={code}&redirect_uri=http://127.0.0.1:8000/zoom/callback/", headers={
        "Authorization": "Basic " + base64_encode("iNQAbBxZT_CxsC9NPA8WVQ:nifYbhIcS83TbfUuqAJmNoIzJmS9bRm6")
    })
    print(data.text)
    request.session["zoom_access_token"] = data.json()["access_token"]

    return redirect('calendar')