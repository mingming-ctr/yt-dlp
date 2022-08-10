

import json
import yt_dlp

import pprint


# 斗罗大陆youtube腾讯官方播放列表
URL = 'https://www.youtube.com/playlist?list=PLMX26aiIvX5oBwyvcxES9P7OvCtHcPny5'

# ℹ️ See help(yt_dlp.YoutubeDL) for a list of available options and public functions
a={}
ydl_opts = {
    "break_per_url":True
}

ydl_opts = {        
    'playlistend': '0',
    'format': 'bestaudio/best',        
    'postprocessors': [{           
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '320',           
        }],   
}
myindex=0
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    print("aaaaaa:",++myindex)
    info = ydl.extract_info(URL, download=False)
    a=info
    # ℹ️ ydl.sanitize_info makes the info json-serializable
    # pprint.pprint(json.dumps(ydl.sanitize_info(info)))


# 斗罗大陆 a["playlist_count"]

# pprint.pprint(a)


urlsearch = "https://www.youtube.com/results?search_query=%E6%96%97%E7%BD%97%E5%A4%A7%E9%99%86+220"


ydl_opts = {        
    'playlistend': '1',
    'format': 'bestvideo/bestaudio',
    'merge_output_format':"mp4" 
}
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    print("aaaaaa:",++myindex)
    info = ydl.extract_info(urlsearch, download=True)
    a=info
    # ℹ️ ydl.sanitize_info makes the info json-serializable
    pprint.pprint(json.dumps(ydl.sanitize_info(info)))



