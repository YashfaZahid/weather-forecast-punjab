import streamlit as st
from datetime import time, date, timedelta
import pandas as pd
import pyodbc
from datetime import datetime

st.set_page_config(page_title="Weather Forecast App", page_icon="⛅")
st.title("⛅ Weather Forecast")

conn_str = (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=localhost\\SQLEXPRESS;"
    "DATABASE=WeatherForecast;"
    "Trusted_Connection=yes;"
)
conn = pyodbc.connect(conn_str)

selected_city = st.selectbox("City", options=["Lahore", "Islamabad", "Multan", "Karachi"])

start_datetime = datetime.today().replace(hour=0, minute=0, second=0, microsecond=0)
end_datetime = start_datetime + timedelta(days=3)
date_list = [start_datetime.date() + timedelta(days=i) for i in range(4)]

query = f"""
SELECT 
    CONVERT(date, [Time]) AS ForecastDate,
    [Min], [Max], [Avg]
FROM [WeatherForecast].[dbo].[{selected_city}]
WHERE CONVERT(date, [Time]) BETWEEN ? AND ?
ORDER BY ForecastDate
"""
df = pd.read_sql(query, conn, params=[start_datetime, end_datetime])

def get_emoji(avg_temp):
    if avg_temp <= 15:
        return "🧊"
    elif 16 <= avg_temp <= 25:
        return "🌤️"
    elif 26 <= avg_temp <= 35:
        return "☀️"
    else:
        return "🔥"

# Display 4 days horizontally
cols = st.columns(4)
for i, target_date in enumerate(date_list):
    row = df[df["ForecastDate"] == target_date]
    with cols[i]:
        st.markdown(f"### {target_date.strftime('%b %d')}")
        if not row.empty:
            r = row.iloc[0]
            emoji = get_emoji(r["Avg"])
            st.markdown(f"# {emoji}")
            st.markdown(f"**Min:** {round(r['Min'], 2)}°C")
            st.markdown(f"**Max:** {round(r['Max'], 2)}°C")
            st.markdown(f"**Avg:** {round(r['Avg'], 2)}°C")
            
        else:
            st.markdown("No data ❌")

selected_date = st.date_input("Date", min_value=date(2016, 1, 1), max_value=date(2027, 12, 31))
hour_options = [time(hour=h, minute=0) for h in range(24)]

if st.button("Submit"):
    date_str = selected_date.strftime('%Y-%m-%d')
    query = f"""
    SELECT 
        CONVERT(date, [Time]) AS ForecastDate,
        [Min], [Max], [Avg]
    FROM [WeatherForecast].[dbo].[{selected_city}]
    WHERE CAST([Time] AS DATE) = ?
    """
    df_selected = pd.read_sql(query, conn, params=[date_str])
    
    st.markdown(f"## Weather Forecast for {selected_date.strftime('%b %d, %Y')}")
    
    if not df_selected.empty:
        r = df_selected.iloc[0]
        emoji = get_emoji(r["Avg"])
        
        # Center content using columns
        col1, col2, col3 = st.columns([1,2,1])
        with col2:
            st.markdown(f"### {selected_date.strftime('%b %d')}")
            st.markdown(f"# {emoji}")
            st.markdown(f"**Min:** {round(r['Min'], 2)}°C")
            st.markdown(f"**Max:** {round(r['Max'], 2)}°C")
            st.markdown(f"**Avg:** {round(r['Avg'], 2)}°C")
            
    else:
        st.markdown("No data available for selected date ❌")
