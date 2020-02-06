import base64
from Crypto.Cipher import AES
from pkcs7 import PKCS7Encoder

text = "Marvin: \"I am at a rough estimate thirty billion times more intelligent than you. Let me give you an example.\" \
Think of a number, any number.\" " \
"Zem: \"Er, five.\" \
Marvin: \"Wrong. You see?\""

key = "AQIDBAUGBwgJCgsMDQ4PEBESExQVFhcYGRqrHB0eHyA="

chiper = "cY1Y1VPXbhUqzYLIOVR0RhUXD5l+dmymBfr1vIKlyqD8KqHUUp2I3dhFXgASdGWzRhOdTj8WWFTJ\
PK0k/GDEVUBDCk1MiB8rCmTZluVHImczlOXEwJSUEgwDHA6AbiCwyAU58e9j9QbN+HwEm1TPKHQ6\
JrIOpdFWoYjS+cUCZfo/85Lqi26Gj7JJxCDF8PrBp/EtHLmmTmaAVWS0ID2cJpdmNDl54N7tg5TF\
TrdtcIplc1tDvoCLFPEomNa5booC"



#encoder = PKCS7Encoder()
#pad_text = encoder.encode(text)
keyEnc = base64.b64decode(key)
cipEnc=base64.b64decode(chiper)

text1 = text[0:16]
chiper1 = cipEnc[0:16]

aes = AES.new(keyEnc,AES.MODE_CBC, text1.encode("utf8"))
iv1 = aes.decrypt(chiper1)
print(iv1)



