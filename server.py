from flask import Flask, render_template, request, redirect

from app_flask.usuarios import Usuario

app=Flask(__name__, template_folder='app_flask')

@app.route('/')
def index():
    return redirect('/users')

@app.route('/users/new')
def new_user():
    return render_template('new_user.html')

@app.route('/user/create',methods=['POST'])
def create():
    print(request.form)
    usuario_id = Usuario.save(request.form)
    return redirect(f'/user/show/{usuario_id}')


@app.route('/users')
def new():
    usuarios = Usuario.get_all()
    return render_template("users.html", usuarios=usuarios)

@app.route('/user/show/<int:user_id>')
def show_user(user_id):
    usuario = Usuario.obtener_por_id(user_id)
    return render_template('show.html', usuario=usuario)

@app.route('/user/edit/<int:user_id>')
def edit_user(user_id):
    usuario = Usuario.obtener_por_id(user_id)
    return render_template('edit.html', usuario=usuario)

@app.route('/user/delete/<int:user_id>')
def delete_user(user_id):
    usuario = Usuario.eliminar_por_id(user_id)
    return redirect('/users')

@app.route('/user/update/<int:user_id>', methods=['POST'])
def update_user(user_id):
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        email = request.form['email']

        Usuario.actualizar_por_id(user_id, nombre, apellido, email)

    return redirect(f'/user/edit/{user_id}')

if __name__=="__main__":
    app.run(debug=True)