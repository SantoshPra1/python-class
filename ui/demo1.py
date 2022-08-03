'''to run this open terminal and type
# streamlit run ui/demo1.py
'''


import streamlit as st
st.title("streamlit demo")
st.header("streamlit is awsome")
st.text("this is simple text example ")
st.write("this is a magical function")
st.markdown("this is a sucess message")
st.success("this is sucess message")
st.info("this is info message")
st.warning("this is warning message")
st.error("this is error message")
st.exception("this is exception message")

#media element
st.image("ui\sample.jpeg")
st.video("https://www.youtube.com/watch?v=NLiJO3y7b-o&list=RDNLiJO3y7b-o&start_radio=1")


#widgets
name =st.text_input("enter the username")
cost =st.number_input("enter the cost")
Comment =st.text_area("enter the remarks ")
status =st.checkbox("save the data")
gender = st.radio("gender",["male","female","other"])


querylist =['how to use streamlit?',
             'Is streamlit free or paid?',
             'Is it gonna rain now?']


query = st.selectbox("what the query",querylist)
rating = st.slider("select the rating",1,5)
btn = st.button("submit the response")
#if btn is pressed

if btn:
    st.write("username:",name)
    st.write("cost:",cost)
    st.write("comment:,comment")
    st.write("status",status)
    st.write("gender:",gender)
    st.write("query:",query)
    st.write('rating:',rating)
