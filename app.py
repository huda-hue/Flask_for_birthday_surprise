from flask import Flask, render_template, request, redirect, url_for

app=Flask(__name__)

@app.route('/')
def index():
	# Halaman awal
	return render_template('index.html')

@app.route('/secret',methods=['GET','POST'])
def secret():
	# Halaman untuk masukkan "kode rahasia"
	if request.method=='POST':
		code=request.form['code']
		if code.lower()=='sayangku': # ganti dgn kode rahasia pilihanmu
			return redirect(url_for('surprise'))
		else:
			return render_template('secret.html',error='Ups, coba lagi ya')
	return render_template('secret.html')

@app.route('/surprise')
def surprise():
	# Halaman kejutan utama
	return render_template('surprise.html')


if __name__=='__main__':
	app.run(debug=True)
