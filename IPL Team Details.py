import requests
from bs4 import BeautifulSoup
team=input('Enter Team name : ')
url=f"https://www.iplt20.com/teams/{team}"
r=requests.get(url)
soup=BeautifulSoup(r.content,"html.parser")
# print(soup)
data=soup.find('div',class_="team-detail-text")

for p in data.find_all('p'):
    span_text = p.find('span').text
    b_text = p.find('b').next_sibling.strip()
    print(span_text,":", b_text)

    '''NOTE : Give team name as "kolkata-knight-riders" for kkr
    "mumbai-indians" for mi....
    '''