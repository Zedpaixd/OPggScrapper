from bs4 import BeautifulSoup
import requests

region = input("What region? (EUW/EUNE/NA/OCE/etc): ").lower()
a = input()
b = a.replace("joined the lobby",",")
p = b.split(",")

print ("\n\n\n")

base1 = "https://"
base2 = ".op.gg/summoner/userName="

for i in range (0,len(p)-1):
    
    res = requests.get(base1+region+base2+p[i])
    link = res.text
    soup = BeautifulSoup(link,'lxml')

    elo1=soup.find('div',class_="SummonerRatingMedium")

    try:
        elo2=elo1.find('div',class_="TierRank")
    except:
        elo2 = ""

    try:
        elo3=elo1.find('span',class_="LeaguePoints")
    except:
        elo3 = ""
    
    try:
        elo4=elo1.find('span',class_="winratio")
    except:
        elo4 = ""

    try:
        c=list(elo3)
    except:
        c=""

    print ("Player name:",p[i])
    
    try:
        print ("Rank:",list(elo2)[0].strip())
    except:
        print ("Does not exist.")
    
    try:
        print (''.join(c).strip())
    except:
        pass
    
    try:
        print (list(elo4)[0].strip(),"\n")
    except:
        pass



