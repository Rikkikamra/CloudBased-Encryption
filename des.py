import pyDes
import string
import random
from datetime import datetime
def id_generator(size=8, chars=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))
def des_encryption(file,val):
    key = id_generator()
    randomkey = pyDes.des(key, pyDes.CBC, "\0\0\0\0\0\0\0\0", pad=None, padmode=pyDes.PAD_PKCS5)
    encryption = randomkey.encrypt(file)
    if val==1:
        keyfile = "first_des_key-" + datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p") + ".txt"
        kout = open("/home/ubuntu/encryption/MultipleKeys/"+keyfile, "w")
        kout.write(key)
        kout.close()
        return encryption,keyfile
    elif val==2:
        filename = "final_encrypted_file-" + datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p") + ".txt"
        keyfile = "second_des_key-" + datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p") + ".txt"
        out = open("/home/ubuntu/encryption/MultipleEncryption/"+filename, "wb")
        kout = open("/home/ubuntu/encryption/MultipleKeys/"+keyfile, "w")
        kout.write(key)
        out.write(encryption)
        out.close()
        kout.close()
        return filename,keyfile
    else:
        filename = "des_file-" + datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p") + ".txt"
        keyfile = "des_key-" + datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p") + ".txt"
        out = open("/home/ubuntu/encryption/EncryptionFiles/"+filename, "wb")
        kout = open("/home/ubuntu/encryption/Keys/"+keyfile, "w")
        kout.write(key)
        out.write(encryption)
        out.close()
        kout.close()
        return filename,keyfile

