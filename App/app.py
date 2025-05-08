import os

from flask import Flask, session, render_template, request, redirect, session, flash, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from flask_session import Session
from sqlalchemy import create_engine, or_
from sqlalchemy.orm import scoped_session, sessionmaker
from models import db, Book, Review, User
import requests

from models import *


app = Flask(__name__)

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
db.init_app(app)

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

Session(app)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/search", methods=["GET", "POST"])
def search():
    """
    change this into a drop down menu function
    with results of pre-loaded brands
    """

    print("Search route hit")
    if request.method == "POST":
        query = request.form.get("query")
        print("user searched", query)
        # case-insensitive partial match on isbn, title, or author
        results = Book.query.filter(
            or_(
                Book.isbn.ilike(f"%{query}%"),
                Book.title.ilike(f"%{query}%"),
                Book.author.ilike(f"%{query}%")
            )
        ).all()
        return render_template("search.html", books=results, query=query)
    return render_template("search.html", books=None)