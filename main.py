import streamlit as st

st.set_page_config(page_title="My Portfolio", page_icon=":briefcase:", layout="centered")

st.title("My Portfolio")

st.subheader("Contact information")
st.write("""
- **Full name**:
- **Phone number**: +998935615464
- **Telegram**: [sinofarmonov](https://t.me/jackson_rodger)
- **Github**: [sinofarmonov](https://github.com/sinofarmonovzfkrvjl)
""")

st.header("Summary")
st.write("""
Self-taught python developer with experience creating APIs. Telegram bots, and web applications. Proficienty in frameworks like FastAPI, streamlit and some Flask, Aiogram
""")

st.header("Skills")
st.write("""
- **Programming languages**: Python, HTML, CSS, Javascript
- **Frameworks and libraries**: FastAPI. aiogram, requests, beautifulsoup4, flask, streamlit, and some more libraries
- **Tools & Platforms**: Git, Telegram bot, Web development, mobile development
""")

st.header("Projects")
st.write("""
- **Full-Media-Downloader-API**: an API that downloads video and images from YouTube, Instagram, Facebook, TikTok, Pinterest and Snapchat made in FastAPI
- **Uzbekistan Weather API**: Provides information about the weather in Uzbekistan, made in FastAPI
- **Full Media Downloader Bot**: Telegram bot that downloads video and images from YouTube, Instagram, Facebook, TikTok, Pinterest and Snapchat, made in aiogram
- **O'zbekiston ob havosi**: weather forcast for Uzbekistan made in FastAPI
- **Gemini AI Chat Bot**: a chat bot web application made in streamlit using gemini api
""")

st.header("Interests")
st.write("""
- Quantum physics, Astrophysics
- Cybersecurity
- Freelance software development
""")

st.divider()