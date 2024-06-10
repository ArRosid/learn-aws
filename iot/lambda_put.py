import boto3

def lambda_handler(event, context):
    client = boto3.client("dynamodb")
    timestamp_str = str(event['timestamp'])
    humidity_str = str(event['humidity'])
    temperature_str = str(event['temperature'])

    response = client.put_item(
        TableName = 'sensor',
        Item = {
            'timestamp': {'S': timestamp_str},
            'humidity': {'S': humidity_str},
            'temperature': {'S': temperature_str}
        }
    )
    return 0
