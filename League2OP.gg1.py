from bs4 import BeautifulSoup
import requests

a = input()
b = a.replace("joined the lobby",",")
p = b.split(",")

base = "https://euw.op.gg/summoner/userName="
for i in range (0,5):
    res = requests.get(base+p[i])
    link = res.text
    soup = BeautifulSoup(link,'lxml')
    elo1=soup.find('div',class_="SummonerRatingMedium")
    elo2=elo1.find('div',class_="TierRank")
    elo3=elo1.find('span',class_="LeaguePoints")
    try:
        c=list(elo3)
    except:
        c=""
    elo4=elo1.find('span',class_="winratio")
    print ("Player name:",p[i])
    try:
        print ("Rank:",list(elo2)[0].strip())
    except:
        pass
    try:
        print (''.join(c).strip())
    except:
        pass
    try:
        print (list(elo4)[0].strip(),"\n\n")
    except:
        pass



