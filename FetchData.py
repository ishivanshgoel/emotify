import requests
import json

class FetchData():
    def __init__(self):
        self.token = '90a7fbaa2164584666dba643898639c6'

    def fetchData(self, _url):
        url = f"https://api.diffbot.com/v3/article?token={self.token}&url={_url}"
        response = requests.get(url)
        jsonData = json.loads(response.content)
        document = jsonData['objects'][0]['text']
        return document, jsonData