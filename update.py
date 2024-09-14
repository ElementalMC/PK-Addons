from bs4 import BeautifulSoup
from datetime import datetime

with open('index.html', 'r') as file:
    soup = BeautifulSoup(file, 'html.parser')

p_tag = soup.find('p')

if p_tag:
    today = datetime.now().strftime('%b %d, %Y')
    
    new_text = f"This site is not owned or operated by ProjectKorra.<br>If you would like to see something added or removed, open a PR or issue on <a href=\"https://github.com/CozmycDev/PK-Addons\">the repo</a>.<br>Legend: <i class=\"fas fa-question-circle\"></i>=Unknown, <i class=\"fa-solid fa-x\"></i>=Dead Link <br>Last Updated: {today}"
    p_tag.string = new_text

    with open('index.html', 'w') as file:
        file.write(str(soup))
