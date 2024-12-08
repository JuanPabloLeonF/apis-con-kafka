from configuration import db
from entities import Product
from flask import request, jsonify, Blueprint, Response
from configuration_kafka import createStockOnApi

productRouter: Blueprint = Blueprint(name="/product/", import_name=__name__, url_prefix="/product/")

class ProductController:

    @staticmethod
    @productRouter.route(rule="/", methods=["GET"])
    def getProducts() -> tuple[Response, int]:
        return jsonify([product.getJSON() for product in Product.query.all()]), 200

    @staticmethod
    @productRouter.route(rule="/", methods=["POST"])
    def createProduct() -> tuple[Response, int]:
        data: dict = request.get_json()

        try:
            product: Product = Product(
                name=data.get("name"),
                price=data.get("price"),
                quantity=data.get("quantity"),
                stock=data.get("stock"),
            )

            db.session.add(product)
            db.session.commit()

            message: dict = {
                "idProduct": product.id,
                "stock": product.stock
            }

            createStockOnApi(message=message)

            return jsonify(product.getJSON()), 201  

        except Exception as error:
            db.session.rollback()
            return jsonify({"message": str(error)}), 400
        finally:
            db.session.close()     