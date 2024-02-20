import streamlit as st

h = st.header(' My Web Site on Diffusion')
s = st.subheader('เว็บไซต์ส่วนตัววววว')
p = st.write('เว็บไซต์นี้แลกมาด้วยหยาดเหงื่อและตวามอดทน')
#banner = st.imge('')
text = st.image('prompt:')
if text:
    st.write('กำลังสร้างภาพ...{text}')
    b = st.button('จะไปต่อหรือ...')
