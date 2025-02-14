import requests
from bs4 import BeautifulSoup
import smtplib
import json
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

CONFIG_FILE = "config.json"
SEEN_NEWS_FILE = "seen_news.txt"

import json

CONFIG_FILE = "config.json"

try:
    with open(CONFIG_FILE, "r", encoding="utf-8") as f:
        CONFIG = json.load(f)
except UnicodeDecodeError:
    print("❌ 檔案編碼錯誤，請確保 `config.json` 是 UTF-8 編碼！")
    exit(1)
except json.JSONDecodeError:
    print("❌ `config.json` 格式錯誤，請檢查 JSON 是否正確！")
    exit(1)

# 確保所有必要的鍵存在
required_keys = ["EMAIL_USER", "EMAIL_PASS", "RECIPIENT_EMAIL", "EMAIL_SUBJECT"]
for key in required_keys:
    if key not in CONFIG:
        print(f"❌ 設定檔缺少 `{key}`，請補上！")
        exit(1)

print("✅ 設定檔載入成功！")


# 讀取設定
if not os.path.exists(CONFIG_FILE):
    print("❌ 找不到設定檔！請先執行 setting.exe 來設定郵件資訊")
    exit(1)


with open("config.json", "r", encoding="utf-8") as f:
    CONFIG = json.load(f)

EMAIL_USER = CONFIG["EMAIL_USER"]
EMAIL_PASS = CONFIG["EMAIL_PASS"]
RECIPIENT_EMAIL = CONFIG["RECIPIENT_EMAIL"]
EMAIL_SUBJECT = CONFIG["EMAIL_SUBJECT"]
EMAIL_BODY = CONFIG["EMAIL_BODY"]

NEWS_SOURCES = {
    "iThome": "https://www.ithome.com.tw/tags/資安週報",
    "InfoSec": "https://www.informationsecurity.com.tw/event/"
}

def fetch_news_ithome():
    """ 爬取 iThome 資安週報 """
    url = NEWS_SOURCES["iThome"]
    response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    soup = BeautifulSoup(response.text, "html.parser")

    latest_news = []
    for article in soup.select(".view-content .title a")[:5]:  # 取前 5 篇
        title = article.text.strip()
        news_url = "https://www.ithome.com.tw" + article["href"]
        if not is_already_sent(news_url):
            latest_news.append((title, news_url))
            save_sent_news(news_url)
    return latest_news

def fetch_news_infosec():
    """ 爬取資安人科技網的最新新聞 """
    url = "https://www.informationsecurity.com.tw/article/article_list.aspx?mod=1"
    response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    soup = BeautifulSoup(response.text, "html.parser")

    latest_news = []
    news_section = soup.find("div", class_="news_list")
    if news_section:
        for article in news_section.find_all("a", href=True)[:5]:
            title = article.text.strip()
            news_url = "https://www.informationsecurity.com.tw" + article["href"]
            if not is_already_sent(news_url):
                latest_news.append((title, news_url))
                save_sent_news(news_url)
    return latest_news

def is_already_sent(news_link):
    """ 檢查新聞是否已經發送過 """
    if not os.path.exists(SEEN_NEWS_FILE):
        return False
    with open(SEEN_NEWS_FILE, "r") as file:
        return news_link in file.read().splitlines()

def save_sent_news(news_link):
    """ 記錄已發送新聞 """
    with open(SEEN_NEWS_FILE, "a") as file:
        file.write(news_link + "\n")

def send_email(news_list):
    """ 發送 Email """
    msg = MIMEMultipart()
    msg["From"] = EMAIL_USER
    msg["To"] = ", ".join(RECIPIENT_EMAIL)
    msg["Subject"] = EMAIL_SUBJECT

    news_content = "\n\n".join([f"{title}\n{link}" for title, link in news_list])
    msg.attach(MIMEText(f"{EMAIL_BODY}\n\n{news_content}", "plain"))

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(EMAIL_USER, EMAIL_PASS)
            server.sendmail(EMAIL_USER, RECIPIENT_EMAIL, msg.as_string())
        print("✅ Email 發送成功！")
    except Exception as e:
        print(f"❌ 發送 Email 失敗：{e}")

def main():
    """ 主程式 """
    ithome_news = fetch_news_ithome()
    infosec_news = fetch_news_infosec()

    all_news = ithome_news + infosec_news
    if all_news:
        send_email(all_news)
    else:
        print("🔍 沒有新的資安新聞")

if __name__ == "__main__":
    main()
