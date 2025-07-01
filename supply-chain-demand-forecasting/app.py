# app.py

import streamlit as st
import pandas as pd
import requests
import plotly.graph_objs as go

st.title("📦 Supply Chain Demand Forecasting")

# File upload
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("### Uploaded Data", df.head())

    sku_id = st.selectbox("Select SKU", df["SKU"].unique())
    model = st.selectbox("Forecasting Model", ["Prophet", "ARIMA"])
    forecast_period = st.slider("Forecast Horizon (weeks)", 4, 52, 12)

    if st.button("Generate Forecast"):
        files = {"file": uploaded_file.getvalue()}
        url = f"http://localhost:5000/forecast/{model.lower()}?sku={sku_id}&period={forecast_period}"
        res = requests.post(url, files=files)
        forecast_df = pd.DataFrame(res.json()["forecast"])

        st.write("### Forecast Output")
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=forecast_df['date'], y=forecast_df['yhat'], name='Forecast'))
        fig.add_trace(go.Scatter(x=forecast_df['date'], y=forecast_df['yhat_upper'], name='Upper Bound', line=dict(dash='dot')))
        fig.add_trace(go.Scatter(x=forecast_df['date'], y=forecast_df['yhat_lower'], name='Lower Bound', line=dict(dash='dot')))
        st.plotly_chart(fig)
