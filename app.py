import streamlit as st
from deep_translator import GoogleTranslator

# Page config
st.set_page_config(page_title="Translator App", page_icon="🌍", layout="centered")

# Session state setup
if "source_lang" not in st.session_state:
    st.session_state.source_lang = "English"

if "target_lang" not in st.session_state:
    st.session_state.target_lang = "Hindi"

if "translated_text" not in st.session_state:
    st.session_state.translated_text = ""

# Title
st.title("🌍 Language Translator")
st.markdown("### Translate text instantly between languages")
st.markdown("---")

# Input
text = st.text_area("Enter text to translate:")

st.caption(f"Characters: {len(text)}")

# Voice input (browser)
st.markdown("### 🎤 Voice Input")
st.info("💡 Press Windows + H and speak")

voice_text = st.text_input("Or speak here:")

if voice_text:
    text = voice_text

# Languages (NO AUTO DETECT)
languages = {
    "English": "en",
    "Hindi": "hi",
    "French": "fr",
    "Spanish": "es",
    "German": "de",
    "Italian": "it",
    "Portuguese": "pt",
    "Russian": "ru",
    "Chinese (Simplified)": "zh-CN",
    "Japanese": "ja",
    "Korean": "ko",
    "Arabic": "ar",
    "Turkish": "tr",
    "Dutch": "nl",
    "Bengali": "bn",
    "Tamil": "ta",
    "Telugu": "te",
    "Marathi": "mr",
    "Gujarati": "gu",
    "Punjabi": "pa",
    "Urdu": "ur"
}

language_names = sorted(languages.keys())

# Dropdowns with session state
col1, col2 = st.columns(2)

with col1:
    st.session_state.source_lang = st.selectbox(
        "From:",
        language_names,
        index=language_names.index(st.session_state.source_lang)
    )

with col2:
    st.session_state.target_lang = st.selectbox(
        "To:",
        language_names,
        index=language_names.index(st.session_state.target_lang)
    )

# Swap button (NOW WORKS)
if st.button("🔄 Swap Languages"):
    st.session_state.source_lang, st.session_state.target_lang = (
        st.session_state.target_lang,
        st.session_state.source_lang,
    )

# Translate
if st.button("Translate"):
    if text.strip() != "":
        try:
            translated = GoogleTranslator(
                source=languages[st.session_state.source_lang],
                target=languages[st.session_state.target_lang]
            ).translate(text)

            st.session_state.translated_text = translated

        except:
            st.error("❌ Translation failed")

    else:
        st.warning("⚠️ Enter text")

# Show result
if st.session_state.translated_text:
    st.success("✅ Translation:")
    st.code(st.session_state.translated_text)

    st.download_button(
        "📋 Copy Translation",
        st.session_state.translated_text
    )

# Reverse translate (NOW WORKS)
if st.session_state.translated_text:
    if st.button("🔁 Reverse Translate"):
        try:
            reversed_text = GoogleTranslator(
                source=languages[st.session_state.target_lang],
                target=languages[st.session_state.source_lang]
            ).translate(st.session_state.translated_text)

            st.success("🔄 Reversed Translation:")
            st.code(reversed_text)

        except:
            st.error("❌ Reverse failed")