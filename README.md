# MES Gateway

### General Information
- Hardware: Orange PI Zero
- MQTT Broker: Mosquitto
- Python Version: 3.7.4

### Strucuture
- MES Gateway Application
- MQTT Broker
- Docker
- Docker Compose
- Environment Variables
    - MQTT_USERNAME
    - MQTT_PASSWORD
    - API_URL
    - API_USERNAME
    - API_PASSWORD

### How it works
The application receives MQTT messages from agents through the local broker, adapts and relays the received data to our platform using HTTP.
