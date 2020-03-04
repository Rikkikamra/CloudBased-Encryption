from Crypto.Cipher import Blowfish
from struct import pack
import random
import string
from datetime import datetime
def id_generator(size=16, chars=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))
def blowfish_encryption(file,val):
	key_str = id_generator()
	key = key_str.encode("utf8")
	bs = Blowfish.block_size
	plaintext = file
	cipher = Blowfish.new(key, Blowfish.MODE_CBC)
	plen = bs - len(plaintext) % bs
	padding = [plen]*plen
	padding = pack('b'*plen, *padding)
	msg = cipher.iv + cipher.encrypt(plaintext + padding)
	if val==1:
		outputFileKey = 'first_blowfish_key-' + datetime.now().strftime('%d-%m-%Y_%I-%M-%S_%p') + '.txt'
		outputFileObj = open("/home/ubuntu/encryption/MultipleKeys/"+outputFileKey, 'wb') #wb to make sure bytes are written
		outputFileObj.write(key)
		outputFileObj.close()
		return msg,outputFileKey
	elif val==2:
		outputFile = 'final_encrypted_file-' + datetime.now().strftime('%d-%m-%Y_%I-%M-%S_%p') + '.txt'
		outputFileKey = 'second_blowfish_key-' + datetime.now().strftime('%d-%m-%Y_%I-%M-%S_%p') + '.txt'
		outputFileObj = open("/home/ubuntu/encryption/MultipleEncryption/"+outputFile, 'wb')
		outputFileObj.write(msg)
		outputFileObj.close()
		outputFileObj = open("/home/ubuntu/encryption/MultipleKeys/"+outputFileKey, 'wb') #wb to make sure bytes are written
		outputFileObj.write(key)
		outputFileObj.close()
		return outputFile,outputFileKey
	else:
		outputFile = 'blowfish_encryption-' + datetime.now().strftime('%d-%m-%Y_%I-%M-%S_%p') + '.txt'
		outputFileKey = 'blowfish_key-' + datetime.now().strftime('%d-%m-%Y_%I-%M-%S_%p') + '.txt'
		outputFileObj = open("/home/ubuntu/encryption/EncryptionFiles/"+outputFile, 'wb')
		outputFileObj.write(msg)
		outputFileObj.close()
		outputFileObj = open("/home/ubuntu/encryption/Keys/"+outputFileKey, 'wb') #wb to make sure bytes are written
		outputFileObj.write(key)
		outputFileObj.close()
		return outputFile,outputFileKey