import openai
import time
# from apify_client import ApifyClient
#
# # https://api.apify.com/v2/acts/epctex~genius-scraper/run-sync?token=apify_api_MtRZVzWeDHIcvbSnJ7cZF7TOPFjBbY39v7NL
# client = ApifyClient("apify_api_MtRZVzWeDHIcvbSnJ7cZF7TOPFjBbY39v7NL")
# run_input = {
#     "startUrls": [
#   ],
#   "search": "God's Plan",
#   "searchMode": "song",
#   "includeComments": false,
#     "proxy": {
#         "useApifyProxy": true
#     },
#     "endPage": 1,
#     "maxItems": 1
# }
# run = client.actor("epctex/genius-scraper").call(run_input=run_input)
#
# print(str(run))


#God's Plan by Drake
lyricsOfSong = """
And, they wishin' and wishin' and wishin' and wishin'
They wishin' on me, yeah
I been movin' calm, don't start no trouble with me
Tryna keep it peaceful is a struggle for me
Don't pull up at 6 AM to cuddle with me
You know how I like it when you lovin' on me
I don't wanna die for them to miss me
Yes, I see the things that they wishin' on me
Hope I got some brothers that outlive me
They gon' tell the story, shit was different with me
God's plan, God's plan
I hold back, sometimes I won't, yeah
I feel good, sometimes I don't, ayy, don't
I finessed down Weston Road, ayy, 'nessed
Might go down a G-O-D, yeah, wait
I go hard on Southside G, yeah, Way
I make sure that north side eat
And still
Bad things
It's a lot of bad things
That they wishin' and wishin' and wishin' and wishin'
They wishin' on me
Bad things
It's a lot of bad things
That they wishin' and wishin' and wishin' and wishin'
They wishin' on me
Yeah, ayy, ayy (ayy)
She say, "Do you love me?" I tell her, "Only partly
I only love my bed and my momma, I'm sorry"
Fifty Dub, I even got it tatted on me
81, they'll bring the crashers to the party
And you know me
Turn a O2 into the O3, dog
Without 40, Oli', there'd be no me
'Magine if I never met the broskis
God's plan, God's plan
I can't do this on my own, ayy, no, ayy
Someone watchin' this shit close, yep, close
I've been me since Scarlett Road, ayy, road, ayy
Might go down as G-O-D, yeah, wait
I go hard on Southside G, ayy, Way
I make sure that north side eat, yuh
And still
Bad things
It's a lot of bad things
That they wishin' and wishin' and wishin' and wishin'
They wishin' on me
Yeah, yeah
Bad things
It's a lot of bad things
That they wishin' and wishin' and wishin' and wishin'
They wishin' on me
Yeah
"""

openai.api_key = "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"
transprosedLyrics = []

lines = lyricsOfSong.splitlines()
source_language = "English" # User Input
target_langauge = "Spanish" # User Input

for line4 in range(0, len(lines), 4):
    chunk = lines[line4:line4+4]
    messages = [
        {"role": "user",
         "content": "Please translate the following provided text in " + source_language + " to " + target_langauge + ":\n" + str(chunk) + "\n END OF TEXT.\nBe absolutely sure to return only the translation."}
    ]
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=messages,
        temperature=0.1,
        max_tokens=4000,
        n=1,
        stop=None,
    )
    print(str(chunk))
    print(response.choices[0].message.content.strip())
    time.sleep(0.5)
    # Fixing it up
    translatedVerse = response.choices[0].message.content.strip()

    prompt = "The following is a chunk of a song in " + source_language + " and its translated counter part in " + target_langauge + ":\n" + source_language + " Verse:\n" + str(chunk) + "\n" + target_langauge + " Translated Verse:\n" + str(translatedVerse) + "\n \n If possible, rewrite the translated verse (still in it's language) so that it more closely matches the cadence of the original language and the syllable count on each line, and try to re-match some of the rhyming that was lost in translation (with synonyms etc.). Make sure the original meaning and number of lines is preserved. Be sure to only return your rewrite."
    messages2 = [
        {"role": "user",
         "content": prompt}
    ]
    response2 = openai.ChatCompletion.create(
        model="gpt-4",
        messages=messages2,
        temperature=0.1,
        max_tokens=4000,
        n=1,
        stop=None,
    )
    print("____")
    print(response2.choices[0].message.content.strip())
    print("----------------------------")
    time.sleep(0.7)

# import os
# #Set Variables
# load_dotenv()
#
# # Set API Keys
# OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
# assert OPENAI_API_KEY, "OPENAI_API_KEY environment variable is missing from .env"
# openai.api_key = "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"
# #Call GPT-4 chat model

