import hmac
import base64
import hashlib

f = open("public.pem")
key = f.read()

str="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJsb2dpbiI6ImFkbWluIn0"

encode = hmac.new(key,str,hashlib.sha256).digest()
sig = base64.urlsafe_b64encode(encode).decode('UTF-8').rstrip("=")

print(str+"."+sig)
