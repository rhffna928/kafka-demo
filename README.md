# kafka-demo
 카프카를 활용해 ROS의 센서데이터를 수집 후 전처리 및 가공 데모



kafka 명령어

토픽 리스트 확인: kafka-topics.sh --list --bootstrap-server localhost:9092

토픽 상세 조회: kafka-topics.sh --describe --topic topic1 --bootstrap-server kafka:9092

토픽 삭제: kafka-topics.sh --delete --bootstrap-server kafka:9092 --topic topic1
