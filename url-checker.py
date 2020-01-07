import os
import requests

def check(url):
    r = requests.get(url)
    return str(r.status_code)

def lambda_handler(event, context):
    url = os.environ['url']
    response_code = os.environ['response_code']
    if check(url) != response_code:
        raise Exception("{url} is down".format(url=url))
