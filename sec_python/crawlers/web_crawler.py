import requests


to_crawl = ['http://g1.globo.com']
crawled = set()

req = requests.get(to_crawl[0])

print(req.text)