import streamlit as st
st.set_page_config(page_title='Cats')
st.header("types od cats")
col1,col2=st.columns(2)
with col1:
  st.subheader("Persian cat")
  st.image("https://static.toiimg.com/thumb/msid-98820330,width-960,height-1280,resizemode-6.cms")
  st.write("persian cats aare cute")
with col2:
  st.subheader("RainBow Rose")
  st.image("https://i0.wp.com/deepgreenpermaculture.com/wp-content/uploads/2018/07/fake-rainbow-rose.jpg?resize=640%2C640&ssl=1")
  st.write("rainbow rose's are very beutiful")
