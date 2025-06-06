import streamlit as st
import pandas as pd
import ast

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

        # Prüfen, ob "Embedding" Spalte vorhanden ist
        if "Embedding" not in df.columns:
            st.error("Die Spalte 'Embedding' wurde nicht gefunden.")
        else:
            # Embedding-Spalte in echte Listen umwandeln
            df["Embedding_vector"] = df["Embedding"].apply(lambda x: ast.literal_eval(x) if isinstance(x, str) else None)

            st.success(f"{len(df):,} Zeilen geladen, Embeddings konvertiert.")
            st.dataframe(df[["Address", "Embedding_vector"]].head())

    except Exception as e:
        st.error(f"Fehler beim Einlesen der Datei: {e}")
else:
    st.info("⬅️ Bitte zuerst eine Datei hochladen.")
