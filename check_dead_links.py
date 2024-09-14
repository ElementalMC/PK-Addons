import requests
import json

CUSTOM_404_SIGNATURES = {
    "github.com": "Page not found",
    "projectkorra.com": "The requested page could not be found."
}

def check_url(url):
    try:
        response = requests.get(url, allow_redirects=True)
        if response.status_code == 404:
            return False 
        
        for domain, signature in CUSTOM_404_SIGNATURES.items():
            if domain in url and signature in response.text:
                print(f"404 detected for {url}")
                return False

        return True

    except requests.RequestException:
        return False 

def update_json(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)

    updated = False
    for entry in data:
        download_url = entry.get('download_url')
        source_url = entry.get('source_url')

        if download_url and not check_url(download_url):
            print(f"Dead link found: {download_url}")
            entry['download_url'] = 'DEAD LINK'
            updated = True

        if source_url and not check_url(source_url):
            print(f"Dead link found: {source_url}")
            entry['source_url'] = 'DEAD LINK'
            updated = True

    if updated:
        with open(file_path, 'w') as f:
            json.dump(data, f, indent=4)
        return True
    return False

if __name__ == "__main__":
    if update_json('forum.json'):
        print("forum.json updated")
    if update_json('github.json'):
        print("github.json updated")
