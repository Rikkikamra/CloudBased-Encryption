from flask import Flask, flash, request, redirect, render_template, send_file
from blowfish import blowfish_encryption
from werkzeug.utils import secure_filename
import os
from tdes import tdes_encryption
from rsa import rsa_encryption
from des import des_encryption


funcdict = {
	'rsa_encryption': rsa_encryption,
	'des_encryption': des_encryption,
	'tdes_encryption': tdes_encryption,
	'blowfish_encryption': blowfish_encryption
}

app = Flask(__name__)
@app.route('/')
def home():
	return render_template("home.html")

@app.route('/homeEnc')
def homeEnc():
	return render_template("home.html")

@app.route('/buttonclick', methods=['POST'])
def buttonclick():
	value = request.form['type']
	if value=="Single Encryption":
		return render_template("profile.html")
	else:
		return render_template("multiple.html")

@app.route('/profile')
def profile():
	return render_template("profile.html")

@app.route('/upload', methods=['POST'])
def upload():
	val = request.form['encryptBtn']
	if val=="RSA Encryption":
		return render_template("upload.html",paraKey=val,first=0,second=0)
	if val=="DES Encryption":
		return render_template("upload.html",paraKey=val,first=0,second=0)
	if val=="Triple DES Encryption":
		return render_template("upload.html",paraKey=val,first=0,second=0)
	if val=="Blowfish Encryption":
		return render_template("upload.html",paraKey=val,first=0,second=0)

@app.route('/encryption', methods=['POST'])
def upload_file():
	encrypt = request.form['encryptType'] 
	first_enc = request.form['firstEnc']
	second_enc = request.form['secondEnc']
	if 'file' not in request.files:
		flash('No file part')
		return redirect(request.url)
	file = request.files['file']
	if first_enc=='0' and second_enc=='0':
		val = 0
		if file:
			file_input = file.read()
			if encrypt=="RSA Encryption":
				encrypt_file,key=rsa_encryption(file_input,val)
			if encrypt=="DES Encryption":
				encrypt_file,key=des_encryption(file_input,val)
			if encrypt=="Triple DES Encryption":
				encrypt_file,key=tdes_encryption(file_input,val)
			if encrypt=="Blowfish Encryption":
				encrypt_file,key=blowfish_encryption(file_input,val)
			return render_template("download.html",file=encrypt_file,key=key)
		else:
			flash('Allowed file types are txt, pdf, png, jpg, jpeg, gif')
			return redirect(request.url)
	else:
		file_input = file.read()
		val =1
		encrypt_first,key1 = funcdict[first_enc](file_input,val)
		val =2
		final_encrypt, key2 = funcdict[second_enc](file_input,val)
		return render_template("downloadMultiple.html",file=final_encrypt,key_first=key1,key_second=key2)


@app.route('/dual',methods=['POST'])
def dual():
	first_enc = request.form['first']
	second_enc = request.form['second']
	if first_enc=='0' and second_enc=='0':
		val = "RSA Encryption"
	else:
		val = "Multiple Encryption"
	return render_template("upload.html", first=first_enc,second=second_enc,paraKey=val)

@app.route('/return_files/<file_enc>/<val>')
def return_files(file_enc,val):
	encrypt = file_enc
	if val=='1':
		try:
			return send_file('EncryptionFiles/'+encrypt,attachment_filename=encrypt,as_attachment=True)
		except Exception as e:
			return str(e)

	elif val=='2':
		try:
			return send_file('MultipleEncryption/'+encrypt,attachment_filename=encrypt,as_attachment=True)
		except Exception as e:
			return str(e)

@app.route('/return_key/<key_enc>/<val>')
def return_key(key_enc,val):
	if val=='1':
		try:
			return send_file('Keys/'+key_enc,attachment_filename=key_enc,as_attachment=True)
		except Exception as e:
			return str(e)
	elif val =='2':
		try:
			return send_file('MultipleKeys/'+key_enc,attachment_filename=key_enc,as_attachment=True)
		except Exception as e:
			return str(e)

@app.route('/return_keym/<keym_enc>')
def return_keym(keym_enc):
	try:
		return send_file('MultipleKeys/'+keym_enc,attachment_filename=keym_enc,as_attachment=True)
	except Exception as e:
		return str(e)


if __name__ == '__main__':
	app.run(host="0.0.0.0", port=80)