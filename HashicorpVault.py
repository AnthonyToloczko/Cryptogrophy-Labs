import os
import base64

def exportEnvVar():
    os.environ["VAULT_ADDR"] = "http://127.0.0.1:8200"
    os.environ["VAULT_TOKEN"] = "hvs.wm7rox2YbHsnaeOFbZO9x9ZV"

def enableTransitEngine():
    os.system("vault secrets enable transit")

def createKey():
    my_key = "my_key"
    os.system("vault write transit/keys/{} type=aes256-gcm96".format(my_key))

def decodeMessage(cipher, key):
    os.system("vault write transit/decrypt/{} ciphertext={}".format(key, cipher))


def encryptMessage(plain, key):
    plain_text = base64.b64encode(bytes(plain, "utf-8"))
    os.system("vault write transit/encrypt/{} plaintext={}".format(key, plain_text.decode("utf-8")))
    
exportEnvVar()
enableTransitEngine()
createKey()
encryptMessage("Hello from Python", "my_key")
decodeMessage("vault:v1:zds+LiAH0Cc6pq1YjU/lkNMvgSRXKb/ywNGL6LIsytu16Q/GuTmeS2Unf1UB", "my_key")
original_text = base64.b64decode("SGVsbG8gZnJvbSBQeXRob24=")
print(original_text.decode())
