import streamlit as st
st.set_page_config(page_title = "MY Streamlit" , page_icon = "random")
st.title("My Streamlit")
mymenu = st.sidebar.selectbox('My menu',("Select List","Home ","FillForm","Downloads"))
if(mymenu=='Home'):
      st.text("This is home page:")

elif(mymenu == "FillForm"):
       with st.form("My Form"):
             name = st.text_input("Enter your name:")
             dob = st.date_input("Enter your dob :")
             marks = st.slider("Choose mark ")
             k = st.form_submit_button("Submit Form ")
             if k:
                   st.write("name ",name ,"DoB ",dob , "marks ",marks)
             
elif(mymenu=="downloads"):
             st.header("Click tO download")
             st.download_button("Download Now ","Hello This is Downloaded data","onlei.txt")
      


      
