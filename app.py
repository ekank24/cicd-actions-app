import streamlit as st
import pandas as pd
import mysql.connector
import os

def fetch_data():
    conn = mysql.connector.connect(
        host=os.getenv('DB_HOST', 'localhost'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_NAME')
    )
    query = "SELECT city, temperature, description, timestamp FROM weather_data WHERE city='Lahti' ORDER BY timestamp DESC LIMIT 100"
    df = pd.read_sql(query, conn)
    conn.close()
    return df

st.set_page_config(page_title="Säädata Lahti", layout="wide")
st.title("Säädata (v1.0)")

try:
    df = fetch_data()
    st.dataframe(df)
    
    st.header("Lämpötilan kehitys")
    chart_df = df.set_index('timestamp')
    st.line_chart(chart_df['temperature'])
except Exception as e:
    st.error(f"Tietokantayhteys epäonnistui tai dataa ei löytynyt: {e}")
