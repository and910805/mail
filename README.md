
# 📧 Security News Mailer

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)](https://www.python.org/)  
[![Requests](https://img.shields.io/badge/Library-requests-green)](https://pypi.org/project/requests/)  
[![BeautifulSoup](https://img.shields.io/badge/Library-BeautifulSoup4-yellowgreen)](https://pypi.org/project/beautifulsoup4/)  
[![SMTP](https://img.shields.io/badge/Email-SMTP-orange)](#)  
[![License](https://img.shields.io/badge/License-MIT-lightgrey)](LICENSE)

---

## 📖 專案簡介
**Security News Mailer** 是一個自動化工具，可以幫助使用者快速掌握最新的資安新聞。  
它會定期從以下來源爬取新聞，並透過 Gmail 自動發送到設定好的收件者信箱：

- 📰 [iThome 資安週報](https://www.ithome.com.tw/tags/資安週報)  
- 🔐 [資安人科技網](https://www.informationsecurity.com.tw/event/)  

### ✅ 適用情境
- 想每天收到最新資安新聞摘要的工程師  
- 公司內部分享資安情資  
- 個人學習資安、追蹤趨勢  

---

## ✨ 功能特色
- 🌐 自動爬取最新資安新聞（iThome / InfoSec）  
- 📨 自動寄送 Email，支援多收件者  
- 📝 使用者可自訂 **標題** 與 **內文**  
- 🔄 防重複機制：避免寄送相同新聞  
- 🖥 提供 **Python 原始碼** 與 **免安裝 EXE**（PyInstaller 打包）  

---

## 📂 專案結構
```

.
├── mail\_test.py      # 主程式：抓取新聞 + 發送 Email
├── setting.py        # 設定工具：互動式生成 config.json
├── config.json       # 郵件帳號與寄送設定（自動產生）
├── seen\_news.txt     # 記錄已寄送過的新聞
├── mail\_test.exe     # 主程式執行檔（免安裝 Python）
├── setting.exe       # 設定工具執行檔（免安裝 Python）
└── README.md         # 專案說明文件

````

---

## ⚙️ 環境需求
- Python 3.8+
- Gmail 帳號（需啟用 [應用程式專用密碼](https://support.google.com/accounts/answer/185833)）
- 必要套件：
  ```bash
    pip install requests beautifulsoup4
  ```

---

## 🚀 使用方法

### 1️⃣ 產生設定檔

執行 `setting.py` 或 `setting.exe`，輸入相關資訊：

```bash
python setting.py
```

會要求輸入以下內容：

* 發送者 Gmail 帳號 / 密碼
* 收件者 Email（可多個，用逗號分隔）
* 郵件主旨
* 郵件內文

執行後會自動生成 `config.json`：

```json
{
  "EMAIL_USER": "yourmail@gmail.com",
  "EMAIL_PASS": "xxxx",
  "RECIPIENT_EMAIL": ["friend1@gmail.com", "friend2@gmail.com"],
  "EMAIL_SUBJECT": "每週資安新聞",
  "EMAIL_BODY": "以下是本週最新的資安新聞"
}
```

📸 執行畫面：
手動執行（需要 Python 環境）
![image](https://github.com/user-attachments/assets/659b7a0d-b810-4f95-be31-e7b8ce99e46c)

---

### 2️⃣ 執行新聞郵件工具

執行 `mail_test.py` 或 `mail_test.exe`：

```bash
python mail_test.py
```

程式流程：

1. 爬取 iThome 與資安人最新新聞
2. 比對 `seen_news.txt` 避免重複
3. 組合成郵件並寄送

---

## 📬 範例輸出

寄送的郵件內容會類似：

```
主旨：每週資安新聞

內文：
以下是本週最新的資安新聞

iThome：零信任架構成為企業防禦主流
https://www.ithome.com.tw/news/123456

InfoSec：AI 驅動的駭客攻擊趨勢
https://www.informationsecurity.com.tw/article/654321
```


---

## 🔒 安全性注意事項

* 請勿將 `config.json` 上傳到公開的 GitHub Repo
* Gmail 帳號請務必使用 **應用程式專用密碼**，不要直接使用真實登入密碼
* 若用於公司內部，建議使用 **郵件 Relay 或 API**（例如 Microsoft Graph、SendGrid）取代直接使用 Gmail

---

## 📝 License

本專案採用 [MIT License](LICENSE)。
請自由修改與使用，但務必保護好郵件帳號資訊。

```

