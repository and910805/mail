import json
import getpass
import os

CONFIG_FILE = "config.json"

def get_user_input(prompt, hide_input=False):
    """ 取得使用者輸入 """
    return getpass.getpass(prompt) if hide_input else input(prompt)

def setup_config():
    """ 設定使用者郵件資訊 """
    config = {}

    print("\n 設定郵件發送資訊")
    config["EMAIL_USER"] = get_user_input("發送者 Email（Gmail）: ")
    config["EMAIL_PASS"] = get_user_input("發送者密碼: ", hide_input=True)
    config["RECIPIENT_EMAIL"] = get_user_input("收件者 Email（用逗號分隔）: ").split(",")

    print("\n 設定郵件格式")
    config["EMAIL_SUBJECT"] = get_user_input("郵件主旨: ")
    config["EMAIL_BODY"] = get_user_input("郵件內文: ")

    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f, indent=4)
    
    print("\n 設定完成！設定已儲存至 config.json")

if __name__ == "__main__":
    setup_config()
