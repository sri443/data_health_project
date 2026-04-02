import streamlit as st
from validator import load_data, validate_data, anomaly_detection

st.set_page_config(page_title="Data Health Monitor", layout="wide")

st.title("📊 Data Health Monitor")

df = load_data()

if df.empty:
    st.warning("No data found. Run data_generator.py first.")
    st.stop()

issues, df = validate_data(df)
anomalies, df = anomaly_detection(df)

# ---- Health Score ----
health_score = 100 - (len(issues) * 20 + len(anomalies) * 2)
health_score = max(0, health_score)

st.metric("Data Health Score", f"{health_score}/100")

# ---- Issues ----
st.subheader("⚠️ Issues Detected")
if issues:
    for issue in issues:
        st.error(issue)
else:
    st.success("No major issues detected")

# ---- Charts ----
st.subheader("📈 Revenue Trend")
st.line_chart(df.set_index("date")["revenue"])

st.subheader("👥 Users Trend")
st.line_chart(df.set_index("date")["users"])

# ---- Anomalies ----
st.subheader("🚨 Revenue Anomalies")
if not anomalies.empty:
    st.dataframe(anomalies[["date", "revenue", "z_score"]])
else:
    st.success("No anomalies detected")

# ---- Raw Data ----
with st.expander("View Raw Data"):
    st.dataframe(df)
