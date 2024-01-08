import streamlit as st
# import matplotlib.pyplot as plt
# import numpy as np
st.set_page_config(page_title='Cats')
#st.header("Types of roses")
st.markdown("<center><h1 style='color:#2D9596;'>RED ROSES</h1></center>", unsafe_allow_html=True)
col1,col2,col3=st.columns(3)
with col1:
  st.markdown("<center><h4 style='color:#EF6262;'>RED ROSES</h4></center>", unsafe_allow_html=True)
  #st.subheader("red roses")
  st.markdown('<img src="https://4.imimg.com/data4/VI/SX/MY-36181633/red-rose.jpg" width=200 height=200>', unsafe_allow_html=True)
  #st.image("https://4.imimg.com/data4/VI/SX/MY-36181633/red-rose.jpg",width=200)
  st.write("red rose is symbol for love")
with col2:
  #st.subheader("RainBow Rose")
  st.markdown("<center><h4 style='color:#EF6262;'>RainBow rose</h4></center>", unsafe_allow_html=True)
  #st.image("https://i0.wp.com/deepgreenpermaculture.com/wp-content/uploads/2018/07/fake-rainbow-rose.jpg?resize=640%2C640&ssl=1",width=200)
  st.markdown('<img src="https://i0.wp.com/deepgreenpermaculture.com/wp-content/uploads/2018/07/fake-rainbow-rose.jpg?resize=640%2C640&ssl=1" width=200 height=200>', unsafe_allow_html=True)
  st.write("rainbow rose's are very beutiful")
with col3:
  #st.subheader("purple Rose")
  st.markdown("<center><h4 style='color:#EF6262;'>Purple rose</h4></center>", unsafe_allow_html=True)
  #st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSXk74GVa0tdXcHmLUVZyGVURs4KfOR54c8gQ&usqp=CAU",width=200)
  st.markdown('<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSXk74GVa0tdXcHmLUVZyGVURs4KfOR54c8gQ&usqp=CAU" width=200 height=200>', unsafe_allow_html=True)
  st.write("purple rose's are awesome")
# data =[1,2,3,4,5,6]
# plt.plot(data)
# st.pyplot(plt)
col1,col2,col3=st.columns(3)
st.image("https://www.eventstodayz.com/wp-content/uploads/2020/03/rose-love-gif.gif")
st.subheader("cultivation of roses")
st.video("https://www.youtube.com/watch?v=fyqttjeM8Ps&pp=ygURcm9zZXMgY3VsdGl2YXRpb24%3D")
