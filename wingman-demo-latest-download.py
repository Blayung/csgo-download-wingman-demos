#!/bin/python3
from requests import get
from bs4 import BeautifulSoup
from bz2 import decompress
from os import remove

#Your replays folder with demos
csgoReplaysFolder='C:\\Program Files (x86)\\Steam\\steamapps\\common\\Counter-Strike Global Offensive\\csgo\\replays'

#Your steamLoginSecure cookie (go to steampowered.com, log in and check the cookies using f12)
steamLoginSecure=''

#Your steam profile ID (go to steampowered.com, enter your profile, and it will be in the url)
profileID=''

url = BeautifulSoup(get(f'https://steamcommunity.com/profiles/{profileID}/gcpd/730/?tab=matchhistorywingman',cookies={"steamLoginSecure":steamLoginSecure}).text,features="lxml").body.select('div.csgo_scoreboard_btn_gotv')[0].parent['href']
print(url)

open('temp.dem.bz2','wb').write(get(url).content)
open(f"{csgoReplaysFolder}/{url[url.rfind('/')+1:-4]}",'wb').write(decompress(open('temp.dem.bz2','rb').read()))
remove('temp.dem.bz2')