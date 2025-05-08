from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship

db = SQLAlchemy()



"""
Classes needed: 
- Brand: name, fabrics, etc (importing raw data from brands)
"""
    
class Brand(db.Model):
    __tablename__ = "brands"
    
    #Define columns
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)  # unique = true toevoegen?
    polyester = db.Column(db.Integer, nullable = False)
    cotton = db.Column(db.Integer, nullable = False)
    polyester = db.Column(db.Integer, nullable = False)
    #mixed = db.Column(db.Integer, nullable = False)
    #want to include how many mixed fabrics they have
    #items analyzed, because i want to include percentages

    #alle fabrics hier toevoegen?
    #dus polyester, cotton, etc? of nieuwe fabric toevoegen elke x als ie een neiwue tegen komt?
    
    def __repr__(self):
        return f"<Book {self.title} by {self.author}, {self.year}>"


