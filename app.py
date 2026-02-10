{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c8e2f931-bc03-4322-80d9-81f287a127e9",
   "metadata": {},
   "outputs": [],
   "source": [
    "import json\n",
    "import urllib.request\n",
    "import streamlit as st\n",
    "from datetime import datetime\n",
    "\n",
    "st.set_page_config(page_title=\"💘 Valentine\", page_icon=\"💘\")\n",
    "\n",
    "# Paste your Google Apps Script Web App URL here:\n",
    "WEB_APP_URL = st.secrets.get(\"WEB_APP_URL\", \"https://script.google.com/macros/s/AKfycbwAkqOqXMlYNW1JpznrpYoXoEAJnw30sVJY2iUOaM4FBPC6R_S3WnvXbY2Xrl4eb7TB/exec\")\n",
    "\n",
    "st.markdown(\"## 💌 A small question…\")\n",
    "st.write(\"I’ve been meaning to ask you something 😊, we spoke about it just thought of making it cute.\")\n",
    "\n",
    "name = st.text_input(\"Your name\")\n",
    "message = st.text_area(\"Optional message back to me\", placeholder=\"Type something cute here…\")\n",
    "\n",
    "st.markdown(\"### Will you be my Valentine MaNkosi? 🌹\")\n",
    "answer = st.radio(\"Choose one:\", [\"Yes 💖\", \"No 🙈\"], horizontal=True)\n",
    "\n",
    "if st.button(\"Submit\", type=\"primary\"):\n",
    "    if not name.strip():\n",
    "        st.warning(\"Please type your name 🙂\")\n",
    "    else:\n",
    "        payload = {\n",
    "            \"name\": name.strip(),\n",
    "            \"answer\": answer,\n",
    "            \"message\": message.strip(),\n",
    "            \"ts\": datetime.now().isoformat(timespec=\"seconds\"),\n",
    "        }\n",
    "\n",
    "        data = json.dumps(payload).encode(\"utf-8\")\n",
    "        req = urllib.request.Request(\n",
    "            WEB_APP_URL,\n",
    "            data=data,\n",
    "            headers={\"Content-Type\": \"application/json\"},\n",
    "            method=\"POST\",\n",
    "        )\n",
    "\n",
    "        try:\n",
    "            with urllib.request.urlopen(req, timeout=10) as resp:\n",
    "                _ = resp.read().decode(\"utf-8\")\n",
    "\n",
    "            if answer.startswith(\"Yes\"):\n",
    "                st.balloons()\n",
    "                st.success(\"YAY 😭💖 I’m smiling so hard right now, details to follow later on the venue.\")\n",
    "            else:\n",
    "                st.info(\"Thank you for being honest 🫶, \")\n",
    "        except Exception as e:\n",
    "            st.error(\"Could not send your response. Check the Web App URL / deployment permissions.\")\n",
    "            st.caption(str(e))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "900b52be-d10c-46d5-abdc-3f4b9e685ae9",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
