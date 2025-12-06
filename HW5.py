import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="AI / Human Detector (Fast Demo)", page_icon="🤖")

# ---------------- 模型初始化（超快版） ----------------
@st.cache_resource
def load_model():
    # Demo 模型：簡單文字特徵判斷
    def predict(text):
        # 字數大於 50 字 → 假設 AI 機率高一些
        prob_ai = min(len(text) / 100, 0.99)
        prob_human = 1 - prob_ai
        return prob_human * 100, prob_ai * 100
    return predict

predict_fn = load_model()

# ---------------- UI ----------------
st.title("🤖 AI / Human Detector (Ultra Fast Demo)")
st.write("輸入一段文本，系統將立即給出 AI / Human 機率。")

text = st.text_area("請輸入內容：", height=200)

if st.button("分析") or text:
    if not text.strip():
        st.warning("請輸入文本再分析。")
    else:
        prob_human, prob_ai = predict_fn(text)

        # ---------------- 結果 ----------------
        st.subheader("📌 偵測結果")
        st.write(f"**AI 可能性：{prob_ai:.2f}%**")
        st.write(f"**Human 可能性：{prob_human:.2f}%**")

        # ---------------- 視覺化 ----------------
        st.subheader("📊 視覺化結果")
        st.progress(prob_ai / 100)

        # 修正 bar_chart 用法
        df = pd.DataFrame({
            "Label": ["Human", "AI"],
            "Probability": [prob_human, prob_ai]
        })
        st.bar_chart(df.set_index("Label"))

        # ---------------- 文本統計 ----------------
        st.subheader("📐 文本統計")
        st.write(f"字數：{len(text)}")
        st.write(f"平均每 50 字 AI 機率（模擬）：{prob_ai:.2f}%")
