from datetime import datetime
import re

def update_html(file_path, replacement_content):
    with open(file_path, 'r') as file:
        content = file.read()
    
    pattern = re.compile(r'<p>.*?</p>', re.DOTALL)
    updated_content = pattern.sub(replacement_content, content)
    
    with open(file_path, 'w') as file:
        file.write(updated_content)

today = datetime.now().strftime('%b %d, %Y')

index_content = f'''
<p>
  This site is not owned or operated by ProjectKorra.<br>If you would like to see something added or removed, open a PR or issue on <a href="https://github.com/CozmycDev/PK-Addons">the repo</a>.<br>Legend: <i class="fas fa-question-circle"></i>=Unknown, <i class="fa-solid fa-x"></i>=Dead Link<br>Last Updated: {today}
</p>
'''

servers_content = f'''
<p>
  This site is not owned or operated by ProjectKorra.<br> If you would like to add, remove, or update a server, feel free to open a PR or issue on <a href="https://github.com/CozmycDev/PK-Addons">the repo</a>.<br>Legend: <i class="fas fa-question-circle"></i>=Unknown, <i class="fa-solid fa-x"></i>=Offline/Not Applicable<br>Last Updated: {today}
</p>
'''

update_html('index.html', index_content)
update_html('servers.html', servers_content)
