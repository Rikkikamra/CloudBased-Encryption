from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
from datetime import datetime
import binascii
keyPair = RSA.generate(3072)
from werkzeug.utils import secure_filename

def rsa_encryption(file,val):
    pubKey = keyPair.publickey()
    pubKeyPEM = pubKey.exportKey()
    privKeyPEM = keyPair.exportKey()    
    msg =file
    encryptor = PKCS1_OAEP.new(pubKey)
    encrypted = encryptor.encrypt(msg)
    if val==1:
        keyfile = "first_rsa_key-" + datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p") + ".txt"
        kout = open("/home/ubuntu/encryption/MultipleKeys/"+keyfile, "wb")
        kout.write(privKeyPEM)
        kout.close()
        return encrypted,keyfile
    elif val==2:
        filename = "final_encrypted_file-" + datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p") + ".txt"
        keyfile = "second_rsa_key-" + datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p") + ".txt"
        out = open("/home/ubuntu/encryption/MultipleEncryption/"+filename, "wb")
        kout = open("/home/ubuntu/encryption/MultipleKeys/"+keyfile, "wb")
        kout.write(privKeyPEM)
        out.write(encrypted)
        out.close()
        kout.close()
        return filename,keyfile
    else:
        filename = "rsa_encryption-" + datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p") + ".txt"
        keyfile = "rsa_key-" + datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p") + ".txt"
        out = open("/home/ubuntu/encryption/EncryptionFiles/"+filename, "wb")
        kout = open("/home/ubuntu/encryption/Keys/"+keyfile, "wb")
        kout.write(privKeyPEM)
        out.write(encrypted)
        out.close()
        kout.close()
        return filename,keyfile