import requests
# url = "https://api.github.com/users/v-senthil"
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
# import feedparser
# from pprint import pprint
# username = "@umangshrestha09"
#
# rss_url = "https://medium.com/feed/"
#
#
# d = feedparser.parse(rss_url +  username)
# if len(d["entries"]) <=2:
# 	print("empty")
# else:
#     print(d)
# for entry in d["entries"]:
#     title = entry["title"]   # title of article
#     link = entry["link"]     # link of article
#     tags = [x["term"] for x in entry["tags"]]  # tags associated with article
#     published_date = entry["published"] # get published date
#     updated_date = entry["updated"] # get last updated date
#     print(title)
#     print(link)



############## Twitter ##################
url = "https://api.twitter.com/2/users/"+ "873477278671421441" +"/tweets?tweet.fields=created_at,lang,source,public_metrics&media.fields=url"
headers = {'Authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAAHm%2FPwEAAAAA%2BiJOwgFvf2dust9tr0vI2Eib%2Bsc%3DG6HL3zlLS2QRtyHrDWEQ9JlPLvj4oPB8MMRIZWAsH1QqiUEuSM'}
response = requests.request("GET", url, headers=headers)
posts = response.json()
data = posts['data']
if 'data' not in posts:
	print("error")
else:
	for i in data:
		print(i['public_metrics']['like_count'])
