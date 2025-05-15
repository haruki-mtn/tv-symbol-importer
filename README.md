# tradingview-symbol-importer

TradingView のウォッチリストに、Excelファイル内の証券コード（シンボル）を自動で追加する Python スクリプトです。

## 概要

このスクリプトは、証券コードを記載した Excel ファイル（例：`symbol.xlsx`）からコードを読み取り、TradingView のウォッチリストに自動追加します。

**注意**  
このスクリプトは [TradingView](https://tradingview.com) の **Essentialプラン以上** で利用可能な機能を補助する目的で作成されています。無料プランで有料機能を模倣・回避することを意図したものではありません。

---

## 使用ライブラリ

```bash
pip install selenium openpyxl
```