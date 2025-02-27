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


## consumer 기본 설정
1. 'test-topic', 토픽명 
2. bootstrap_servers : 자신의 서버 설정란
3. auto_offset_reset : default 값은 latest
earliest : 가장 처음 offset 부터 데이터 가져오기
latest   : 가장 마지막 offset 부터 데이터 가져오기
None     : 해당 consumer group이 가져가고자 하는 topic의 consmer offset 정보가 없으면 exception을 발생시킴.
4. enable_auto_commit : defalut 값은 true 자동으로 offset을 커밋하는 옵션이다.
카프카 컨슈머 서버는 기본적으로 들어온 메시지를 특정 DB에 기록하는 역할을 수행한다.
만약 로직이 동작하는 과정에서 에러가 발생을 하게 된다면, 해당 offset은 커밋이 되어서는 안된다.
그러기 때문에 로직이 다 진행이 되고 원하는 시점에 커밋을 하는 방식을 사용하는 것이 맞다고 생각
