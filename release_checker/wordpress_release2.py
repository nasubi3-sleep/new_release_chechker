from bs4 import BeautifulSoup
import requests

url = "https://ja.wordpress.org/download/releases/"
response = requests.get(url)
response.raise_for_status()

# HTML解析
soup = BeautifulSoup(response.text, "html.parser")

# id="latest" のセクションを取得
latest_section = soup.find("div", {"id": "latest"})
if not latest_section:
    raise ValueError("最新リリースのセクションが見つかりません。")

# 最新リリースのテーブルから最初の行を取得
table = latest_section.find("table")
if not table:
    raise ValueError("最新リリースのテーブルが見つかりません。")

# テーブルの最初の行（trタグ）
latest_row = table.find("tbody").find("tr")

# バージョン情報を取得
version = latest_row.find("th", {"class": "wp-block-wporg-release-tables__cell-version"}).text.strip()

# 結果を表示
print(f"最新バージョン: {version}")
