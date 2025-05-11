# tradingview-watchlist-bot

TradingView のウォッチリストに、Excelファイル内の証券コードを自動で追加する Python スクリプトです（Selenium使用）。

## 概要

このスクリプトは、証券コードを記載した Excel ファイル（例：`stock-code.xlsx`）からコードを読み取り、Selenium 経由で TradingView のウォッチリストに自動追加します。

**注意**  
このスクリプトは [TradingView](https://tradingview.com) の **Professionalプラン以上** で利用可能な機能（CSV/コードの一括追加）を補助する目的で作成されています。無料プランで有料機能を模倣・回避することを意図したものではありません。

---

## 必要環境

- Python 3.8+
- Google Chrome
- ChromeDriver（バージョンはChromeに合わせてください）
- TradingView アカウント（ログイン済みプロファイルを使用）
- Excelファイル（例：`stock-code.xlsx`）

## 使用ライブラリ

```bash
pip install selenium openpyxl
```