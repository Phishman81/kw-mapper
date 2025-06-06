import streamlit as st
import pandas as pd

st.set_page_config(page_title="Keyword-to-URL Mapper MVP", layout="wide")

st.title("🔍 Keyword-to-URL Mapper")
st.markdown("Lade eine Screaming Frog CSV mit Embeddings hoch, um loszulegen.")

uploaded_file = st.file_uploader(
    "📤 CSV-Datei auswählen (Screaming Frog Export)",
    type=["csv"]
)

if uploaded_file:
    try:
        df = pd.read_csv(uploaded_file)
        st.success(f"{len(df):,} Zeilen geladen.")
        st.dataframe(df.head())
    except Exception as e:
        st.error(f"Fehler beim Einlesen der Datei: {e}")
else:
    st.info("⬅️ Bitte zuerst eine Datei hochladen.")
