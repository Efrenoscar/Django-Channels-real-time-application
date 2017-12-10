from django.http import HttpResponse
from channels.handler import AsgiHandler

def http_consumer(message):
    response = HttpResponse("Hellow World! You asked for %s" % message.content['path'])
    for chunk in AsgiHandler.encode_response(response):
        message.reply_channel.send(chuck)
