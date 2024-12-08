from configuration import db
from entities import Stock
from flask import request, jsonify, Blueprint, Response

stockRouter: Blueprint = Blueprint(name="/stock/", import_name=__name__, url_prefix="/stock/")

class StockController:

    @stockRouter.route(rule="/", methods=["GET"])
    def getStocks() -> tuple[Response, int]:
        return jsonify([stock.getJSON() for stock in Stock.query.all()]), 200       