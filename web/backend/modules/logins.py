import json
from flask import Flask
from flask.ext.mysql import MySQL
def checklogin(mysql,login,password):
    cur = mysql.connect().cursor()
    try:
        cur.execute("select login,password from users where login='{}' and password='{}'".format(login,password))
        answer='Вход выполнен успешно'
        return answer
    except:
        answer='Данная связка логин/пароль не найдена в базе данных'
        return answer

def registration(mysql, login, password):
    cur = mysql.connect().cursor()
    try:
        cur.execute("select login from users where login='{}'".format(login))
        cur.execute("""INSERT INTO users(login,password) values({},{})""".format(login, password))
        answer='Регистрация прошла успешно'
        return answer
    except:
        answer = 'Данная связка логин и пароль уже существует'
        return answer
