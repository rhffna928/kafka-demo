from kafka import KafkaConsumer

consumer = KafkaConsumer(
    'test',
    bootstrap_servers=['172.22.0.6:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='test-group'
)

for message in consumer:
    print(f"Partition: {message.partition}, Received: {message.value.decode('utf-8')}")
