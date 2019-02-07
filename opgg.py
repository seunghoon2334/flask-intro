import requests
from bs4 import BeautifulSoup
url = 'http://www.op.gg/summoner/userName='
userName = 'hide on bush'
requests.get(url)
response = requests.get(url+userName).text
soup = BeautifulSoup(response, 'html.parser')
wins = soup.select_one('#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.TierBox.Box > div.SummonerRatingMedium > div.TierRankInfo > div.TierInfo > span.WinLose > span.wins')
losses = soup.select_one('#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.TierBox.Box > div.SummonerRatingMedium > div.TierRankInfo > div.TierInfo > span.WinLose > span.losses')
print(wins.text)
print(losses.text)