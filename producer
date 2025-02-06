from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers=['localhost:9092', 'localhost:9093', 'localhost:9094'],
    value_serializer=lambda v: v.encode('utf-8')
)

for i in range(5):
    future = producer.send('test', value=f'Message {i}')
    result = future.get(timeout=10)  # 오류 발생 시 예외 출력
    print(f"Sent: {result}")

producer.flush()
producer.close()
