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
    items_analyzed = db.Column(db.Integer, nullable=False, default=0)

    # Fabric colums : niet zeker of dit wel de juiste manier is om dit te doen hoor
    polyester = db.Column(db.Integer, nullable = False, default=0)
    cotton = db.Column(db.Integer, nullable = False, default=0)
    polyester = db.Column(db.Integer, nullable = False, default=0)

    #mixed = db.Column(db.Integer, nullable = False)
    mixed_fabrics_count = db.Column(db.Integer, nullable=False, default=0)
    materials_per_item_avg = db.Column(db.Float, nullable=False, default=0.0)
    #want to include how many mixed fabrics they have
    #items analyzed, because i want to include percentages

    #alle fabrics hier toevoegen?
    #dus polyester, cotton, etc? of nieuwe fabric toevoegen elke x als ie een nieuwe tegen komt?
    
    def __repr__(self):
        return f"<Brand {self.name}>"


