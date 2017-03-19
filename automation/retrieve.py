import json

def url(event, context):

    body = {
        'url': '...',
    }

    response = {
        'statusCode': 200,
        'body': json.dumps(body)
    }

    return response
