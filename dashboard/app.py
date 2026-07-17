import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# --- CONFIG ---
st.set_page_config(page_title="Ethiopia FI Dashboard", layout="wide")

# --- MOCK DATA ---
years = list(range(2011, 2025))
ownership = [12, 14, 16, 22, 23, 24, 25, 27, 30, 32, 33, 34, 35, 48]
df = pd.DataFrame({'Year': years, 'Ownership': ownership})

# --- NAVIGATION ---
st.sidebar.title("Dashboard Sections")
section = st.sidebar.radio("Navigate to:", ["Overview", "Trends", "Forecasts", "Inclusion Projections"])

# --- PAGE 1: OVERVIEW ---
if section == "Overview":
    st.title("Financial Inclusion Overview")
    c1, c2, c3 = st.columns(3)
    c1.metric("Current Ownership", "48.0%", "+13.0%")
    c2.metric("P2P/ATM Crossover", "1.4x", "Stable")
    c3.metric("Annual Growth", "3.8%", "Positive")
    
    st.markdown("### Executive Summary")
    st.write(
        "This interactive dashboard enables stakeholders to track financial inclusion progress, "
        "assess historical developments, analyze scenario forecasts, and measure strategic progress "
        "toward national development targets."
    )

# --- PAGE 2: TRENDS ---
elif section == "Trends":
    st.title("Historical Trends")
    fig = px.line(df, x='Year', y='Ownership', title="Account Ownership Over Time", markers=True)
    fig.update_xaxes(rangeslider_visible=True) # Interactive Date Range Selector
    st.plotly_chart(fig, use_container_width=True)
    
    # Data Download functionality
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button("Download Historical Data (CSV)", csv, "historical_data.csv", "text/csv")

# --- PAGE 3: FORECASTS ---
elif section == "Forecasts":
    st.title("Projections & Confidence Intervals")
    model = st.selectbox("Select Scenario", ["Baseline", "Optimistic", "Pessimistic"])
    
    proj_years = [2025, 2026, 2027]
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=proj_years, y=[51, 54, 57], name="Central Forecast", line=dict(dash='dash')))
    fig.add_trace(go.Scatter(x=proj_years, y=[49, 51, 53], name="Lower Bound", line=dict(color='red')))
    st.plotly_chart(fig, use_container_width=True)

# --- PAGE 4: INCLUSION PROJECTIONS ---
elif section == "Inclusion Projections":
    st.title("60% Inclusion Target Tracker")
    
    # 1. Scenario Selector
    scenario = st.select_slider("Select Scenario:", ["Pessimistic", "Base", "Optimistic"])
    
    # 2. Gauge Visualization
    val = 52.0 if scenario == "Pessimistic" else 55.5 if scenario == "Base" else 59.5
    fig = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = val,
        title = {'text': f"Projected 2027 Inclusion Rate ({scenario})"},
        gauge = {'axis': {'range': [40, 65]}, 'bar': {'color': "darkcyan"}}
    ))
    st.plotly_chart(fig, use_container_width=True)
    
    # 3. Answering the Consortium's Key Questions
    st.markdown("---")
    st.subheader("Consortium Insights")
    
    with st.expander("Q: What is the primary driver of these projections?"):
        st.write("Mobile money ecosystem expansion (Telebirr/M-Pesa) remains the primary accelerator. Infrastructure parity (4G/5G) acts as the critical foundation for these gains.")
        
    with st.expander("Q: What risks threaten the 60% target?"):
        st.write("Macro-economic volatility (inflation) and potential delays in rural telecom infrastructure rollout are the top identified risks that could push performance toward the Pessimistic scenario.")
        
    with st.expander("Q: What is the recommended strategic pivot?"):
        st.write("Shift from a purely ownership-based expansion to a utility-focused growth strategy, prioritizing digital payment volumes as a leading indicator of inclusion sustainability.")
