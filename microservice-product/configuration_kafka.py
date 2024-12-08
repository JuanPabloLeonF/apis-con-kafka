from kafka.producer import KafkaProducer
import json

producer: KafkaProducer = KafkaProducer(
        bootstrap_servers=['localhost:9092'],
        value_serializer=lambda value: json.dumps(value).encode('utf-8'),
        api_version=(0, 0, 1),
    )

def createStockOnApi(message: dict):
    try:
        metadata = producer.send(
            topic="stock_create_product",
            value=message
        )
        producer.flush()
    except Exception as e:
        print(f"Error sending message: {str(e)}")

