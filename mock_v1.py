import streamlit as st
import asyncio

st.title("4 AI Compare")

q = st.text_area("質問")

if st.button("送信"):
    col1,col2 = st.columns(2)
    with col1:
        st.subheader("ChatGPT")
        st.write(call_openai(q))

        st.subheader("Claude")
        st.write(call_claude(q))

    with col2:
        st.subheader("Gemini")
        st.write(call_gemini(q))

        st.subheader("Grok")
        st.write(call_grok(q))


