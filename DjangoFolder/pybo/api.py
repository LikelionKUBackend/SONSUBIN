import requests

q="침착맨"

google_api_key="api"
request_url=f"https://www.googleapis.com/youtube/v3/search?key={google_api_key}" \
            f"&textFormat=plainText&part=snippet&q={q}"
json_data=requests.get(request_url)
json_data=json_data.json()

channelId=json_data["items"][0]["id"]["channelId"]

request_url2=f"https://www.googleapis.com/youtube/v3/activities?key={google_api_key}" \
    f"&textFormat=plainText&part=snippet&channelId={channelId}"

json_data2=requests.get(request_url2)
json_data2=json_data2.json()

Data=json_data2["items"]

videoTitle=[]
for i in range(2,len(Data)):
    data=Data[i]
    videoTitle.append(data["snippet"]["title"])

videoTitle=list(set(videoTitle))

for i in videoTitle:
    print(i)

