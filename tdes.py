import string
import random
from datetime import datetime
from Crypto.Cipher import DES3
from Crypto import Random

def id_generator(size=16, chars=string.ascii_uppercase + string.digits):
     return ''.join(random.choice(chars) for _ in range(size))

def tdes_encryption(file,val):
	key = id_generator()
	data = file
	iv =Random.new().read(DES3.block_size)
	cipher_encrypt = DES3.new(key, DES3.MODE_OFB, iv)
	encrypt = cipher_encrypt.encrypt(data)
	cipher_decrypt = DES3.new(key, DES3.MODE_OFB, iv) 
	decrypt=cipher_decrypt.decrypt(encrypt)
	if val==1:
		keyfile = "first_tdes_key-" + datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p") + ".txt"
		kout = open("/home/ubuntu/encryption/MultipleKeys/"+keyfile, "w")
		kout.write(key)
		kout.close()
		return encrypt,keyfile
	elif val==2:
		filename = "final_encrypted_file-" + datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p") + ".txt"
		keyfile = "second_tdes_key-" + datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p") + ".txt"
		out = open("/home/ubuntu/encryption/MultipleEncryption/"+filename, "wb")
		kout = open("/home/ubuntu/encryption/MultipleKeys/"+keyfile, "w")
		kout.write(key)
		out.write(encrypt)
		out.close()
		kout.close()
		return filename,keyfile
	else:
		filename = "tdes_file-" + datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p") + ".txt"
		keyfile = "tdes_key-" + datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p") + ".txt"
		out = open("/home/ubuntu/encryption/EncryptionFiles/"+filename, "wb")
		kout = open("/home/ubuntu/encryption/Keys/"+keyfile, "w")
		kout.write(key)
		out.write(encrypt)
		out.close()
		kout.close()
		return filename,keyfile