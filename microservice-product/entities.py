from configuration import db
import uuid

class Product(db.Model):

    id: str = db.Column(db.String, primary_key=True, default=lambda: str(uuid.uuid4()))
    name: str = db.Column(db.String, nullable=False)
    price: float = db.Column(db.Float, nullable=False)
    quantity: int = db.Column(db.Integer, nullable=False)
    stock: int = db.Column(db.Integer, nullable=False)

    def getJSON(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "quantity": self.quantity,
            "stock": self.stock
        }