import streamlit as st
st.set_page_config(page_title='Cats')
st.header("Types of roses")
col1,col2,col3=st.columns(3)
with col1:
  st.subheader("red roses")
  st.image("https://4.imimg.com/data4/VI/SX/MY-36181633/red-rose.jpg")
  st.write("red rose is symbol for love")
with col2:
  st.subheader("RainBow Rose")
  st.image("https://i0.wp.com/deepgreenpermaculture.com/wp-content/uploads/2018/07/fake-rainbow-rose.jpg?resize=640%2C640&ssl=1")
  st.write("rainbow rose's are very beutiful")
with col3:
  st.subheader("purple Rose")
  st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSXk74GVa0tdXcHmLUVZyGVURs4KfOR54c8gQ&usqp=CAU")
  st.write("purple rose's are awesome")
