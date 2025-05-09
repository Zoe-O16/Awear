import csv
import os
from flask import Flask, render_template, request
from models import *
from create import *

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

#hier moet ik mn scraping tool gaan gebruiken
#dus scrapen, csv maken

def main():
    with open("books.csv", mode="r", encoding="utf-8") as f:
        reader = csv.reader(f)
        next(reader) #skip header

        for isbn, title, author, year in reader:
            #create a new Book instance
            book = Book(isbn=isbn, title=title, author=author, year=int(year))
            db.session.add(book)
            print(f"Added book: {title} by {author}, ISBN: {isbn}, Year: {year}")

        # Commit the session to save the data to the database
        db.session.commit()

if __name__ == "__main__":
    with app.app_context():
        main()