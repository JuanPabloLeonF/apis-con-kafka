from kafka import KafkaConsumer
import os
import json
from configuration import db
from entities import Stock

def runConsumer():
    from main import app
    stockConsumer: KafkaConsumer = KafkaConsumer(
            "stock_create_product",
            bootstrap_servers=['localhost:9092'],
            value_deserializer=lambda value: json.loads(value.decode('utf-8')),
            api_version=(0,0,1),
            group_id="stock_group",
            enable_auto_commit=False
        )

    with app.app_context():
        for message in stockConsumer:
            try:
                print(f"Received message: {message.value}")
                if message.value:
                    data = message.value
                    stock = Stock(
                        idProduct=data.get("idProduct"),
                        stock=data.get("stock"),
                    )
                    db.session.add(stock)
                    db.session.commit()
                    print(f"Stock for Product {stock.idProduct} added successfully.")
                    stockConsumer.commit()
            except Exception as e:
                db.session.rollback()
                print(f"Error processing stock message: {str(e)}")
            finally:
                db.session.close()
