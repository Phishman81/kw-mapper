import streamlit as st
import pandas as pd

st.set_page_config(page_title="KW-Mapper", layout="wide")
st.title("🔗 Keyword-zu-URL Mapper")

# File uploader
uploaded = st.file_uploader(
    "Lade deine Embeddings-CSV oder -XLSX hoch", 
    type=["csv", "xlsx"]
)

if uploaded:
    try:
        if uploaded.name.lower().endswith(".csv"):
            df = pd.read_csv(uploaded)
        else:
            df = pd.read_excel(uploaded)
    except Exception as e:
        st.error(f"Fehler beim Einlesen: {e}")
    else:
        st.success("Datei erfolgreich geladen!")
        st.write("Vorschau deiner Daten:")
        st.dataframe(df.head(10))
        st.write(f"Spalten: {', '.join(df.columns)}")
