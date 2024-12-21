# 返ってくる内容が想定と違うが、最新版は取れていそう

from bs4 import BeautifulSoup
import requests

# 対象URL
url = "https://www.elastic.co/downloads/past-releases#elasticsearch"

# Webページを取得
response = requests.get(url)
response.raise_for_status()

# HTMLを解析
soup = BeautifulSoup(response.text, "html.parser")

# class=release-notes-container を持つ div を取得
release_notes_container = soup.find("div", class_="release-notes-container")

if release_notes_container:
    # class=title-wrapper を持つ div を取得
    title_wrapper = release_notes_container.find("div", class_="title-wrapper")
    
    if title_wrapper:
        # 配下にある h3 タグを取得
        h3_tag = title_wrapper.find("h3")
        
        if h3_tag:
            print(h3_tag.text.strip())
        else:
            print("title-wrapper の配下に h3タグが見つかりませんでした")
    else:
        print("release-notes-container の配下に title-wrapper が見つかりませんでした")
else:
    print("release-notes-container が見つかりませんでした")
