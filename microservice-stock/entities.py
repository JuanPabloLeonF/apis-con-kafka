from configuration import db
import uuid

class Stock(db.Model):

    id: str = db.Column(db.String, primary_key=True, default=lambda: str(uuid.uuid4()))
    idProduct: str = db.Column(db.String, nullable=False)
    stock: int = db.Column(db.Integer, nullable=False)

    def getJSON(self) -> dict:
        return {
            "id": self.id,
            "idProduct": self.idProduct,
            "stock": self.stock
        }