from datetime import datetime
import json

def lambda_handler(event, context):
    
    time_string = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return {
        "statusCode": 200,
        "body": json.dumps('The time is now ' + time_string + ' UTC.')
    }
