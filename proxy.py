import os
from os.path import join, dirname
from dotenv import load_dotenv
from sanic import Sanic
from sanic.response import json, text
from logzero import logger

app = Sanic()
dotenv_path = join(dirname(__file__), '.config')
load_dotenv(dotenv_path)


@app.route("/")
async def proxy(request):
    return json([
        {
            'action': 'connect',
            'from': os.environ['FROM'],  # must be a Nexmo virtual number
            'endpoint': [{
                'type': 'phone',
                'number': os.environ['TO']
            }]
        }
    ])


@app.route("/events", methods=['POST'])
async def events(request):
    event = request.json

    direction = {
        'inbound': "⇠",
        'outbound': "⇢"
    }.get(event.get('direction'), "🤷")

    def log(status):
        if status in ['started', 'ringing']:
            return logger.debug
        elif status in ['answered', 'complete']:
            return logger.info
        elif status in ['machine', 'unanswered', 'busy']:
            return logger.warn
        elif status in ['failed', 'timeout', 'rejected']:
            return logger.error
        else:
            return logger.debug

    log(event['status'])(f'{ event["status"] } {direction} ({ event["conversation_uuid"] })')

    return text(f'POST request - {request.json}')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
