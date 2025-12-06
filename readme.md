# AI / Human Detector (Fast Demo)

🤖 **AI / Human Detector** 是一個基於 Streamlit 的簡單文字 AI 偵測 Demo，用於判斷輸入文本的 **AI 生成可能性** 與 **Human 撰寫可能性**。此版本為 **超快模擬版**，透過文字長度做簡單判斷，適合作為展示與快速測試使用。

🔗 [線上體驗 Demo](https://ai-detector-iczm9u6xqr5kmmphimyzva.streamlit.app/)

---

## 專案功能

- 輸入文字 → 立即顯示 AI% / Human% 機率
- 顯示進度條與長條圖視覺化結果
- 文本統計資訊（字數、模擬 AI 機率）
- 簡單、快速，適合展示與學習

---

## 專案架構 (建議)

```
AI-Detector/
│
├── HW5.py                # Streamlit 主程式
├── requirements.txt      # Python 套件依賴
├── README.md             # 專案說明文件
└── .gitignore            # 忽略檔案設定
```

---

## 安裝與使用

1. **Clone 專案到本地**

```bash
git clone https://github.com/Eating-thinker/AI-Detector.git
cd AI-Detector
```

2. **建立虛擬環境（可選）**

```bash
python -m venv venv
source venv/bin/activate      # Linux / Mac
venv\Scripts\activate         # Windows
```

3. **安裝依賴套件**

```bash
pip install -r requirements.txt
```

> 推薦最小安裝版本的 `requirements.txt`：
```
streamlit==1.39.0
pandas
numpy
scikit-learn
```

4. **啟動 Streamlit Demo**

```bash
streamlit run HW5.py
```

---

## 使用說明

1. 在文字方塊輸入任意文本。
2. 按下 **分析** 或直接輸入文字。
3. 系統會立即顯示：
   - **AI 可能性**
   - **Human 可能性**
   - 視覺化長條圖與進度條
   - 文本統計（字數與模擬 AI 機率）

---

## 線上 Demo

- 🔗 [體驗 Demo](https://ai-detector-iczm9u6xqr5kmmphimyzva.streamlit.app/)

---

## 注意事項

- 本版本使用 **簡單文字長度判斷** 模擬 AI 機率，**不是真實 AI 偵測模型**。
- 若要使用真實 AI 偵測，可結合：
  - `scikit-learn` TF-IDF + LogisticRegression
  - `transformers` 模型（需安裝 `torch` / `transformers` 套件）
- 在 Streamlit Cloud 上部署時，安裝大型套件（如 `torch`）可能會失敗，建議先測試最小版依賴。

---

## 建議改進方向

- 將文字長度判斷替換為 **TF-IDF + 機器學習模型**，提高判斷精準度
- 整合 **transformers 預訓練模型**（例如 GPT-2/3 判斷特徵）
- 增加 **多語言支援** 或 **更豐富的文本統計**
- 將結果可視化升級成 **圓餅圖或雷達圖**，增加互動性

---

## 聯絡方式

- GitHub: [Eating-thinker/AI-Detector](https://github.com/Eating-thinker/AI-Detector)
- 若有問題，可在 Issues 提問，我會儘快回覆。
