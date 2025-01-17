# kafka-demo
 카프카를 활용해 센서데이터를 수집 후 전처리 및 가공 데모



## kafka 명령어

토픽 생성:
kafka-topics.sh --create --topic [토픽명] --bootstrap-server localhost:9092 --replication-factor [개수] --partitions [개수]

토픽 리스트 확인:
kafka-topics.sh --list --bootstrap-server localhost:9092

토픽 상세 조회: 
kafka-topics.sh --describe --topic [토픽명] --bootstrap-server kafka:9092

토픽 삭제: kafka-topics.sh --delete --bootstrap-server kafka:9092 --topic [토픽명]
