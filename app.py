import json
import urllib.request
import streamlit as st
from datetime import datetime

st.set_page_config(page_title="💘 Valentine", page_icon="💘")

# Reads from .streamlit/secrets.toml
WEB_APP_URL = st.secrets["WEB_APP_URL"]

st.markdown("## 💌 A small question…")
st.write("I’ve been meaning to ask you something 😊, I spoke to you about it but thought it would be cute to do this.")

name = st.text_input("Your name")
message = st.text_area("Optional message back to me", placeholder="Type something cute here…")

st.markdown("### Will you be my Valentine? 🌹")
answer = st.radio("Choose one:", ["Yes 💖", "No 🙈"], horizontal=True)

if st.button("Submit", type="primary"):
    if not name.strip():
        st.warning("Please type your name 🙂")
    else:
        payload = {
            "name": name.strip(),
            "answer": answer,
            "message": message.strip(),
            "ts": datetime.now().isoformat(timespec="seconds"),
        }

        data = json.dumps(payload).encode("utf-8")
        req = urllib.request.Request(
            WEB_APP_URL,
            data=data,
            headers={"Content-Type": "application/json"},
            method="POST",
        )

        try:
            with urllib.request.urlopen(req, timeout=10) as resp:
                resp.read()

            if answer.startswith("Yes"):
                st.balloons()
                st.success("YAY 😭💖 I’m smiling so hard right now, Ngigcwele ngawe uyezwa MaNkosi?")
            else:
                st.info("Thank you for being honest 🫶")
        except Exception as e:
            st.error("Could not send your response. Check your WEB_APP_URL deployment permissions.")
            st.caption(str(e))
