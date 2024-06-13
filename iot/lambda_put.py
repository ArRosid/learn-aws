import boto3

def lambda_handler(event, context):
    client = boto3.client("dynamodb")
    timestamp_str = str(event['timestamp'])
    humidity_str = str(event['humidity'])
    temperature_str = str(event['temperature'])
    fire_intensity_str = str(event['fire_intensity'])
    gasconcentration_str = str(event['gasconcentration'])
    
    response = client.put_item(
        TableName = 'sensor',
        Item = {
            'timestamp': {'S': timestamp_str},
            'humidity': {'S': humidity_str},
            'temperature': {'S': temperature_str},
            'fire_intensity': {'S': fire_intensity_str},
            'gasconcentration': {'S': gasconcentration_str}
        }
    )
    return 0
