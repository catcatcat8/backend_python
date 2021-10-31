import json
from datetime import datetime

def app(environ, start_response):
    start_response('200 OK', [('Content-Type', 'application/json')])
    
    current_time = datetime.now()
    data = {
        "time": str(current_time),
        "url": environ["HTTP_HOST"]
    }
    json_data = json.dumps(data)

    json_utf = str.encode(json_data)
    yield json_utf
