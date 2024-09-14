from datetime import datetime
import re

with open('index.html', 'r') as file:
    content = file.read()

today = datetime.now().strftime('%b %d, %Y')

p_content = f'''
<p>
  This site is not owned or operated by ProjectKorra.<br>If you would like to see something added or removed, open a PR or issue on <a href="https://github.com/CozmycDev/PK-Addons">the repo</a>.<br>Legend: <i class="fas fa-question-circle"></i>=Unknown, <i class="fa-solid fa-x"></i>=Dead Link<br>Last Updated: {today}
</p>
'''

pattern = re.compile(r'<p>.*?</p>', re.DOTALL)

content = pattern.sub(p_content, content)

with open('index.html', 'w') as file:
    file.write(content)
