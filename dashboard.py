import streamlit as st
import requests

st.set_page_config(page_title="📈 Dashboard Sinyal XAUUSD", layout="centered")
st.title("📊 Sinyal Price Action (XAUUSD)")

# Fetch data
try:
    res = requests.get("https://REPLIT-URL.koyeb.app/sinyal")  # GANTI DENGAN URL REPLIT API kamu
    sinyal = res.json()
except:
    sinyal = {}

for tf in ["m5", "m15"]:
    if tf in sinyal:
        st.subheader(f"⏱ Timeframe: {tf.upper()}")
        data = sinyal[tf]
        col1, col2 = st.columns(2)
        col1.metric("Arah", data["arah"])
        col2.metric("Confidence", f"{data['confidence']}%")

        st.markdown(f"""
        - Entry: `{data['entry']}`  
        - SL: `{data['sl']}`  
        - TP1: `{data['tp1']}`  
        - TP2: `{data['tp2']}`  
        - TP3: `{data['tp3']}`  
        - Strategi: `{data['strategi']}`  
        - Time: `{data['timestamp']}`
        """)
    else:
        st.warning(f"Sinyal belum tersedia untuk TF {tf.upper()}")
