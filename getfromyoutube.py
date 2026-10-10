#Youtube　APIへのリクエスト　json形式でレスポンスをもらう
def requestforyoutube()
    import requests
#youtube apiへのリクエスト送信
url = "https://www.googleapis.com/youtube/v3"
payload = {"key1":"value1", "key2":"value2"}
#api上で指定の動画を検索する
search.list()
channnelID="channnelID"
type=video
publishedafter=today
publishedbefore=tomorrow
order=date

#リクエストをもらう
r = requests.get(url, params=payload)
r.json()
