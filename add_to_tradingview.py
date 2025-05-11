from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import openpyxl

# Excelファイルから証券コードを取得
wb = openpyxl.load_workbook("stock-code.xlsx")
ws = wb.active
codes = [str(cell.value).zfill(4) for cell in ws["B"][1:] if cell.value]

# Chromeの設定
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_argument("--user-data-dir=C:/chrome-dev-profile")
options.add_argument("--profile-directory=Default")

# ドライバ起動
service = Service(executable_path="C:/Tools/chromedriver/chromedriver.exe")
driver = webdriver.Chrome(service=service, options=options)
driver.get("https://jp.tradingview.com/")

# 数秒待機（ページの完全読み込み）
wait = WebDriverWait(driver, 15)
time.sleep(10)  # 初回読み込みだけ少し長めに待つ

# シンボルの追加ボタンを押す
add_symbol_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[aria-label='シンボルの追加']")))
add_symbol_button.click()

for code in codes:
    try:
        # モーダル内の検索ボックスに証券コードを入力
        search_box = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='text'][placeholder='検索']")))
        search_box.clear()
        search_box.send_keys(code)
        search_box.send_keys(Keys.ENTER)
        time.sleep(2)

        # ウォッチリストに追加ボタンを押す
        add_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "span.addAction-oRSs8UQo")))
        add_button[0].click()
        time.sleep(1)

    except Exception as e:
        print(f"{code} でエラー: {e}")
        continue

print("完了")
driver.quit()
