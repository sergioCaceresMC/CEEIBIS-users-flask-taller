from flask import Blueprint, render_template, request, jsonify, redirect, url_for, flash
from utils.db import db

from models.user_model import User
from sqlalchemy import select

user = Blueprint("user", __name__)

@user.route("/")
def home():
    return render_template("main.html")

@user.route("/login", methods=['GET','POST'])
def login():
    if request.method == 'POST':
        try:
            # Comprobar si la contraseña es correcta
            query = select(User).where((
                User.username == request.username and 
                User.password == request.password
            ))
            user_result = db.session.execute(query)

        except:
            return render_template("auth.html")

    else:
       return render_template("auth.html")

@user.route("/new", methods = ['GET', 'POST'])
def create_user():
    if request.method == 'POST':
        try:
            #Creamos el usuario
            username = request.form['username']
            name = request.form['name']    
            lastname = request.form['lastname']
            email = request.form['email']
            user_new = User(
                name=name, 
                lastname=lastname, 
                username=username, 
                email=email
            )
            db.session.add(user_new)
            db.session.commit()
            return redirect(url_for('user.users'))
        except:
            flash("Error al crear nuevo usuario")
            return render_template("new.html")
    else:
        return render_template("new.html")

@user.route("/users", methods=["GET"])
def users():
    try:
        query = select(User)
        result = db.session.execute(query).scalars().all()
        print(result)
        return render_template("users.html", users=result)
    except Exception as e:
        print(e)
        flash("Error al obtener el listado de usuarios")
        return render_template("users.html", users=[])

@user.route("/edit/<string:user_id>", methods=["GET", "POST"])
def set_user(user_id):
    try:
        query = select(User).where(User.id == user_id)
        result = db.session.execute(query).scalar_one_or_none()

        if not result:
            flash("Usuario no encontrado")
            return redirect(url_for("user.users"))

        if request.method == "POST": 
            result.username = request.form["username"]
            result.email = request.form["email"]
            result.name = request.form["name"]
            result.lastname = request.form["lastname"]

            db.session.commit()
            flash("Usuario actualizado correctamente")
            return redirect(url_for("user.users"))

        # mostrar formulario con datos actuales
        return render_template("edit.html", user=result)

    except Exception as e:
        print('hola', e)
        db.session.rollback()
        flash("Error al actualizar el usuario")
        return redirect(url_for("user.users"))

@user.route("/delete/<string:user_id>", methods=["POST"])
def delete_user(user_id):
    try:
        user = db.session.query(User).filter_by(id=user_id).first()

        if not user:
            flash("Usuario no encontrado")
            return redirect(url_for("user.users"))

        db.session.delete(user)
        db.session.commit()

        flash("Usuario eliminado correctamente")
        return redirect(url_for("user.users"))

    except Exception as e:
        db.session.rollback()
        flash("Error al borrar el usuario")
        return redirect(url_for("user.users"))
