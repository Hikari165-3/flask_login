from flask import Flask, session,render_template,request,url_for,redirect

app=Flask(__name__)
app.secret_key='clave_secreta_muy_segura'

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/set_session',methods=['POST'])
def set_session():
    session['username']='Maria'
    session['password']='123'
    
    user=request.form.get('user')
    contrasena=request.form.get('contrasena')
    if session['username']==user and session['password']==contrasena:
        username=session.get('username')
        return render_template('welcome.html',username=username)
    else:
        return 'No se encontro al usuario<br><a href="/">Vaciar el carrito</a>'

@app.route('/salir')
def salir():
    session.pop('username',None)
    return redirect(url_for('index'))

if __name__=="__main__":
    app.run(debug=True,port='5020')