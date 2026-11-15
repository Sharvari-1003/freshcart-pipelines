import pika
import json
import random
import time
from datetime import datetime

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host="localhost")
)
channel = connection.channel()

channel.exchange_declare(
    exchange="rapido-dispatch",
    exchange_type="topic",
    durable=True
)

cities = ["bangalore", "chennai"]
zones = ["koramangala", "indiranagar", "whitefield", "tnagar"]
types = ["ride", "food"]

print("D3 Dispatcher started...")

try:
    count = 1

    while True:
        if count % 10 == 0:
            # Ensure malformed messages reach Bangalore consumers
            city = "bangalore"
            zone = "koramangala"
            request_type = "food"
        else:
            city = random.choice(cities)
            zone = random.choice(zones)
            request_type = random.choice(types)

        routing_key = f"{city}.{zone}.{request_type}"

        message = {
            "id": count,
            "city": city,
            "type": request_type,
            "ts": datetime.now().isoformat()
        }

        if count % 10 != 0:
            message["zone"] = zone
        else:
            print(f"Sending malformed message #{count} (zone missing)")

        channel.basic_publish(
            exchange="rapido-dispatch",
            routing_key=routing_key,
            body=json.dumps(message),
            properties=pika.BasicProperties(delivery_mode=2)
        )

        print(f"Published #{count}: {routing_key} | {message}")

        count += 1
        time.sleep(2)

except KeyboardInterrupt:
    print("Dispatcher stopped.")

finally:
    connection.close()
