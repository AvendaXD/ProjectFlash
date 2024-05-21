from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/biblioteca')
def juegos():
    return render_template('biblioteca.html')

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        #Obtener los datos
        nombre = request.form['nombre']
        email = request.form['email']
        password = request.form['password']
        return redirect('/login')
    else:
        #solicitud GET
        return render_template('registro.html')
    
@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/fancypants')
def fancy():
    return render_template('fancypants.html')

@app.route('/cooperativos')
def coop():
    return render_template('cooperativos.html')

@app.route('/mario')
def mario():
    return render_template('mario.html')

@app.route('/henrystickmin')
def henry():
    return render_template('henrystickmin.html')

@app.route('/sonic')
def sonic():
    return render_template('sonic.html')

@app.route('/biblioteca2')
def juegos2():
    return render_template('biblioteca2.html')


@app.route('/smash')
def smash():
    return render_template('smash.html')

@app.route('/flipline')
def flipline():
    return render_template('flipline.html')

@app.route('/disparos')
def disparos():
    return render_template('disparos.html')

@app.route('/random')
def random():
    return render_template('random.html')

if __name__ == '__main__':
    app.run(debug=True)