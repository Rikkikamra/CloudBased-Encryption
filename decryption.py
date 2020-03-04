from Crypto.Cipher import Blowfish
from struct import pack
output = 'actualText.txt'
bs = Blowfish.block_size
inputKey = 'key1.txt'
inputFile = 'encryption.txt'

fileObj = open(inputKey, errors="ignore")
content = fileObj.read()
fileObj.close()

fileObj = open(inputFile, errors="ignore")
contentCipher = fileObj.read()
fileObj.close()

ciphertext = contentCipher.encode() #encode() to convert the string to bytes
cipherkey = content.encode("utf8")
# print(ciphertext)
iv = ciphertext[:bs]
ciphertext = ciphertext[bs:]

# msg2 = b"".join(cipherkey.decrypt_cbc(ciphertext, iv))

cipher = Blowfish.new(cipherkey, Blowfish.MODE_CFB, iv)
msg1 = cipher.decrypt(ciphertext)

last_byte = ciphertext[-1]
msg = ciphertext[:- (last_byte if type(last_byte) is int else ord(last_byte))]
# print(repr(msg))
print(last_byte)
# print(msg2)