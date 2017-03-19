import json

def retrieve_url(event, context):

    body = {
        'url': '...',
    }

    response = {
        'statusCode': 200,
        'body': json.dumps(body)
    }

    return response

def create_url(event, context):

    body = {
        'url': '...',
    }

    response = {
        'statusCode': 201,
        'body': json.dumps(body)
    }

    return response
