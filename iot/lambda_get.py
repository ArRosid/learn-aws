import json
import boto3

def lambda_handler(event, context):
    if event['resource'] == '/data' and event['httpMethod'] == 'GET':
        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table('sensor')

        try:
            # Scan DynamoDB table to retrieve all items
            response = table.scan()

            # Extract items from response
            items = response['Items']

            # Return a response
            return {
                "statusCode": 200,
                "body": json.dumps(items)
            }
        except Exception as e:
            # Return an error response
            return {
                "statusCode": 500,
                "body": json.dumps({"error": str(e)})
            }
    else:
        # Return a response for invalid resource or method
        return {
            "statusCode": 404,
            "body": json.dumps({"error": "Resource not found or method not allowed"})
        }
