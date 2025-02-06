from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)

# Modelo de Usuário
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)

# Rota principal - Lista os usuários
@app.route('/')
def index():
    users = User.query.all()
    return render_template('index.html', users=users)

# Criar um novo usuário
@app.route('/add', methods=['POST'])
def add_user():
    name = request.form['name']
    email = request.form['email']
    new_user = User(name=name, email=email)
    db.session.add(new_user)
    db.session.commit()
    return redirect(url_for('index'))

# Atualizar um usuário
@app.route('/update/<int:id>', methods=['POST'])
def update_user(id):
    user = User.query.get(id)
    user.name = request.form['name']
    user.email = request.form['email']
    db.session.commit()
    return redirect(url_for('index'))

# Deletar um usuário
@app.route('/delete/<int:id>')
def delete_user(id):
    user = User.query.get(id)
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
