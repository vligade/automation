import json

def url(event, context):

    body = {
        'url': '...',
    }

    response = {
        'statusCode': 201,
        'body': json.dumps(body)
    }

    return response
