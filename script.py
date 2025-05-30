from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import openpyxl
import time
import random

# ランダムに遅延を発生させる関数
def human_sleep(base=1.0, variance=0.5):
    time.sleep(base + random.uniform(0, variance))

# Excelファイルから証券コード（シンボル）を取得
wb = openpyxl.load_workbook("symbol.xlsx")
ws = wb.active
codes = [str(cell.value).zfill(4) for cell in ws["B"][1:] if cell.value]

# Chromeの設定
options = webdriver.ChromeOptions()
options.add_argument("--user-data-dir=C:/chrome-dev-profile")
options.add_argument("--profile-directory=Default")

# WebDriverの設定
service = Service(executable_path="C:/Tools/chromedriver/chromedriver.exe")
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://jp.tradingview.com/")

# 該当要素が見つかるまで待機する設定
wait = WebDriverWait(driver, 15)

# ウォッチリスト上部にある「シンボルの追加」ボタンを押す
add_symbol_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[aria-label='シンボルの追加']")))
add_symbol_btn.click()
human_sleep()

for i, code in enumerate(codes):
    try:
        # モーダル内の検索ボックスにシンボルを入力
        search_box = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='text'][placeholder='検索']")))
        search_box.clear()
        search_box.send_keys(code)
        human_sleep()
        search_box.send_keys(Keys.ENTER)
        human_sleep()

        # 検索結果一覧を取得
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.exchangeName-oRSs8UQo")))
        suggestions = driver.find_elements(By.CSS_SELECTOR, "div.exchangeName-oRSs8UQo")

        # 「ウォッチリストに追加」ボタンを押す
        added = False
        for suggestion in suggestions:
            text = suggestion.text
            if "TSE" in text:
                try:
                    add_watchlist_btn = suggestion.find_element(By.CSS_SELECTOR, "span.addAction-oRSs8UQo")
                    add_watchlist_btn.click()
                    human_sleep()
                    print(f"{code} を追加しました")
                    added = True
                    break
                except Exception as e:
                    print(f"{code} の追加失敗: {e}")
        if not added:
            print(f"{code} のTSE銘柄が見つかりませんでした")

        # 意図的な遅延
        if (i + 1) % 10 == 0:
            print("クールダウン中...")
            time.sleep(10)

    except Exception as e:
        print(f"{code} でエラー: {e}")

print("完了")
driver.quit()
