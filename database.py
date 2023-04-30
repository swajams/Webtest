from flask import Flask, render_template, request, redirect, url_for, flash
from sqlalchemy import create_engine, text

# Change this according to your MySQL Workbench
DB_USER = 'root'
DB_PASS = 'E^^hnikh1984'
DB_NAME = 'movietest'

engine = create_engine(f"mysql+pymysql://{DB_USER}:{DB_PASS}@localhost/{DB_NAME}")

# Testing if you run this .py
with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM movietest.users"))
    print(result.all())

def insert(id, name, num):
    with engine.connect() as conn:
        query = text(f"INSERT INTO movietest.users (idusers, usernames, passwords) VALUES ('{id}', '{name}', '{num}');")
        conn.execute(query)
        conn.commit()


def display_data():
    with engine.connect() as conn:
        result = conn.execute(text(f"SELECT * FROM movietest.users"))
        users = result.fetchall()
    return render_template('home.html', users=users)
        

