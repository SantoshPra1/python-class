import streamlit as st
from textblob import TextBlob

def get_all_nouns(blob):
    noun =[]
    for tag in blob.tags:
        if tag[1] =='NN':
            nouns.append(tag[0])
    return nouns        

def get_sentiment(blob):
    polarity < 0:
    return ' negative 🤩'
elif polarity ==0:
    return 'neutral😏'
else:
    return 'positive😴'


def spell_check(text):
    words    


# streamlit run nlp.py
st.sidebar.title("NLP using TextBlob")
msg =st.text_area("enter something in english",height=300)
if st.button("update"): 
    st.sidebar.subheader("your content")
    st.sidebar.write(msg)
if msg:
    blob =textblob(msg)
    tag =blob.tags
    st.subheader("part of speech tagging:nouns")
    st.write(get_all_nouns(blob))
