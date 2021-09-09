import requests
# url = "https://api.github.com/users/v-senthil"
# headers = {
#    'Authorization': 'token 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'
# }
# response = requests.request("GET", url, headers=headers)
# data = response.json()
# print(response.status_code)
# print(data['name'])


# url = "https://dev.to/api/articles?username=senthil_v1"
# headers = {'api-key': 'DweJQwcBMRd9uFxFAA2Yh4hn'}
# response = requests.request("GET", url, headers=headers)
# data = response.json()
# print(response.text)
# print(len(response.text))


############# Medium #################
import feedparser
from pprint import pprint
username = "@umangshrestha09"

rss_url = "https://medium.com/feed/"


d = feedparser.parse(rss_url +  username)
if len(d["entries"]) <=2:
	print("empty")
else:
    print(d)
# for entry in d["entries"]:
#     title = entry["title"]   # title of article
#     link = entry["link"]     # link of article
#     tags = [x["term"] for x in entry["tags"]]  # tags associated with article
#     published_date = entry["published"] # get published date
#     updated_date = entry["updated"] # get last updated date
#     print(title)
#     print(link)
