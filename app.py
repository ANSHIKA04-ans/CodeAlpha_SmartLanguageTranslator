import streamlit as st
from deep_translator import GoogleTranslator

st.set_page_config(page_title="Smart Language Translator", page_icon="🌍")

st.title("🌍 Smart Language Translator")
st.write("Translate text into multiple languages instantly.")

languages = {
    "English": "en",
    "Hindi": "hi",
    "French": "fr",
    "Spanish": "es",
    "German": "de",
    "Japanese": "ja",
    "Chinese": "zh-CN"
}

if "history" not in st.session_state:
    st.session_state.history = []

text = st.text_area("Enter Text")

col1, col2 = st.columns(2)

with col1:
    source_lang = st.selectbox(
        "Source Language",
        list(languages.keys())
    )

with col2:
    target_lang = st.selectbox(
        "Target Language",
        list(languages.keys())
    )

st.write(f"Characters: {len(text)}")
st.write(f"Words: {len(text.split())}")

if st.button("Translate"):
    if text.strip():
        translated = GoogleTranslator(
            source=languages[source_lang],
            target=languages[target_lang]
        ).translate(text)

        st.success("Translation")
        st.write(translated)

        st.session_state.history.append(
            f"{source_lang} → {target_lang}: {translated}"
        )
    else:
        st.warning("Please enter text.")

st.subheader("Translation History")

for item in reversed(st.session_state.history):
    st.write(item)