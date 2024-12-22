import os
import json
import boto3

def lambda_handler(event, context):
    # Checking if running locally
    if os.environ.get('AWS_SAM_LOCAL'):
        # Use local DynamoDB endpoint
        dynamodb = boto3.resource('dynamodb', endpoint_url='http://172.17.0.1:8000')
    else:
        # Use the default DynamoDB endpoint (AWS)
        dynamodb = boto3.resource('dynamodb')

    # Parse the JSON body
    body = json.loads(event['body'])

    # Access the Id element
    item_id = body['Id']

    # Deleting item on DynamoDB
    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])
    response = table.delete_item(Key={'Id': item_id})

    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'Item deleted', 'response': response})
    }