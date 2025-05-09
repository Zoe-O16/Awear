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
    drop down menu function with results of pre-loaded brands
    """

    print("Search route hit")
    if request.method == "POST":
        brand = request.form.get("brand")
        score = get_score(brand)
        # Changed to match HTML code (adjusted from books)
        return render_template("search.html", selected_brand=brand, score=score, brands=get_brand_info())
    #Changed to match HTML
    return render_template("search.html", score=None)
    #insert way of handling a non-input, maybe with a gentle instruction


def get_brand_info():
    """
    gets brand info from scraper
    """

def get_score(brand):
    """
    Should query database and calculate it 
    """
    scores = {
        "Mango": 35,
        "Patagonia": 90,
        "Levi's": 70,
    }
    #Score op basis van 
    #   hoeveelheid natuurlijke vs. onnatuurlijke materialen (eigenlijk moeten hier percenategs bij in de scraper dan)
    #   de hoeveelheid materialen per item gemiddeld, 
    #   alle materialen in het algemeen met een waarde per merk
    #   zoek online naar score voor bepaalde materialen
    #dit moet dan geanalyseerd worden op basis van hoeveelheid items die gechecked zijn

