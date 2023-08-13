from apify_client import ApifyClient

userinputSong = input("Please input a song: ")
print("Finding Lyrics for: '" + userinputSong + "'")
# https://api.apify.com/v2/acts/epctex~genius-scraper/run-sync?token=apify_api_MtRZVzWeDHIcvbSnJ7cZF7TOPFjBbY39v7NL
client = ApifyClient("apify_api_MtRZVzWeDHIcvbSnJ7cZF7TOPFjBbY39v7NL")
run_input = {
    "startUrls": [
  ],
  "search": userinputSong,
  "searchMode": "song",
  "includeComments": False,
    "proxy": {
        "useApifyProxy": True
    },
    "endPage": 1,
    "maxItems": 1
}
run = client.actor("epctex/genius-scraper").call(run_input=run_input)

print(str(run))
