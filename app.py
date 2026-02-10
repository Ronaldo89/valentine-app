{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "c8e2f931-bc03-4322-80d9-81f287a127e9",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2026-02-10 11:25:11.264 WARNING streamlit.runtime.scriptrunner_utils.script_run_context: Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
     ]
    },
    {
     "ename": "StreamlitSecretNotFoundError",
     "evalue": "No secrets found. Valid paths for a secrets.toml file or secret directories are: C:\\Users\\rgebashe.ic\\.streamlit\\secrets.toml, C:\\Users\\rgebashe.ic\\Desktop\\Python\\Vali vali\\.streamlit\\secrets.toml",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mStreamlitSecretNotFoundError\u001b[0m              Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[3], line 9\u001b[0m\n\u001b[0;32m      6\u001b[0m st\u001b[38;5;241m.\u001b[39mset_page_config(page_title\u001b[38;5;241m=\u001b[39m\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m💘 Valentine\u001b[39m\u001b[38;5;124m\"\u001b[39m, page_icon\u001b[38;5;241m=\u001b[39m\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m💘\u001b[39m\u001b[38;5;124m\"\u001b[39m)\n\u001b[0;32m      8\u001b[0m \u001b[38;5;66;03m# Paste your Google Apps Script Web App URL here:\u001b[39;00m\n\u001b[1;32m----> 9\u001b[0m WEB_APP_URL \u001b[38;5;241m=\u001b[39m st\u001b[38;5;241m.\u001b[39msecrets\u001b[38;5;241m.\u001b[39mget(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mWEB_APP_URL\u001b[39m\u001b[38;5;124m\"\u001b[39m, \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mhttps://script.google.com/macros/s/AKfycbwAkqOqXMlYNW1JpznrpYoXoEAJnw30sVJY2iUOaM4FBPC6R_S3WnvXbY2Xrl4eb7TB/exec\u001b[39m\u001b[38;5;124m\"\u001b[39m)\n\u001b[0;32m     11\u001b[0m st\u001b[38;5;241m.\u001b[39mmarkdown(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m## 💌 A small question…\u001b[39m\u001b[38;5;124m\"\u001b[39m)\n\u001b[0;32m     12\u001b[0m st\u001b[38;5;241m.\u001b[39mwrite(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mI’ve been meaning to ask you something 😊, we spoke about it just thought of making it cute.\u001b[39m\u001b[38;5;124m\"\u001b[39m)\n",
      "File \u001b[1;32m~\\AppData\\Local\\anaconda3\\Lib\\_collections_abc.py:811\u001b[0m, in \u001b[0;36mMapping.get\u001b[1;34m(self, key, default)\u001b[0m\n\u001b[0;32m    809\u001b[0m \u001b[38;5;124m'\u001b[39m\u001b[38;5;124mD.get(k[,d]) -> D[k] if k in D, else d.  d defaults to None.\u001b[39m\u001b[38;5;124m'\u001b[39m\n\u001b[0;32m    810\u001b[0m \u001b[38;5;28;01mtry\u001b[39;00m:\n\u001b[1;32m--> 811\u001b[0m     \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[38;5;28mself\u001b[39m[key]\n\u001b[0;32m    812\u001b[0m \u001b[38;5;28;01mexcept\u001b[39;00m \u001b[38;5;167;01mKeyError\u001b[39;00m:\n\u001b[0;32m    813\u001b[0m     \u001b[38;5;28;01mreturn\u001b[39;00m default\n",
      "File \u001b[1;32m~\\AppData\\Local\\anaconda3\\Lib\\site-packages\\streamlit\\runtime\\secrets.py:470\u001b[0m, in \u001b[0;36mSecrets.__getitem__\u001b[1;34m(self, key)\u001b[0m\n\u001b[0;32m    464\u001b[0m \u001b[38;5;250m\u001b[39m\u001b[38;5;124;03m\"\"\"Return the value with the given key. If no such key\u001b[39;00m\n\u001b[0;32m    465\u001b[0m \u001b[38;5;124;03mexists, raise a KeyError.\u001b[39;00m\n\u001b[0;32m    466\u001b[0m \n\u001b[0;32m    467\u001b[0m \u001b[38;5;124;03mThread-safe.\u001b[39;00m\n\u001b[0;32m    468\u001b[0m \u001b[38;5;124;03m\"\"\"\u001b[39;00m\n\u001b[0;32m    469\u001b[0m \u001b[38;5;28;01mtry\u001b[39;00m:\n\u001b[1;32m--> 470\u001b[0m     value \u001b[38;5;241m=\u001b[39m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_parse()[key]\n\u001b[0;32m    471\u001b[0m     \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m \u001b[38;5;28misinstance\u001b[39m(value, Mapping):\n\u001b[0;32m    472\u001b[0m         \u001b[38;5;28;01mreturn\u001b[39;00m value\n",
      "File \u001b[1;32m~\\AppData\\Local\\anaconda3\\Lib\\site-packages\\streamlit\\runtime\\secrets.py:372\u001b[0m, in \u001b[0;36mSecrets._parse\u001b[1;34m(self)\u001b[0m\n\u001b[0;32m    366\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m found_secrets_file:\n\u001b[0;32m    367\u001b[0m     error_msg \u001b[38;5;241m=\u001b[39m (\n\u001b[0;32m    368\u001b[0m         secret_error_messages_singleton\u001b[38;5;241m.\u001b[39mget_no_secrets_found_message(\n\u001b[0;32m    369\u001b[0m             file_paths\n\u001b[0;32m    370\u001b[0m         )\n\u001b[0;32m    371\u001b[0m     )\n\u001b[1;32m--> 372\u001b[0m     \u001b[38;5;28;01mraise\u001b[39;00m StreamlitSecretNotFoundError(error_msg)\n\u001b[0;32m    374\u001b[0m \u001b[38;5;28;01mfor\u001b[39;00m k, v \u001b[38;5;129;01min\u001b[39;00m secrets\u001b[38;5;241m.\u001b[39mitems():\n\u001b[0;32m    375\u001b[0m     \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_maybe_set_environment_variable(k, v)\n",
      "\u001b[1;31mStreamlitSecretNotFoundError\u001b[0m: No secrets found. Valid paths for a secrets.toml file or secret directories are: C:\\Users\\rgebashe.ic\\.streamlit\\secrets.toml, C:\\Users\\rgebashe.ic\\Desktop\\Python\\Vali vali\\.streamlit\\secrets.toml"
     ]
    }
   ],
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
