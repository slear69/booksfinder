import streamlit as st
st.title("Библиотека")
if "books" not in st.session_state:
  st.session_state.books=[]
st.header("добави книга")
title = st.text_input("Зглавие")
author = st.text_input("Автор")
price  = st.number_input("цена")
if st.button("Добави книга"):
  book ={
    "title": title,
    "author": author,
    "price": price,
  }
  st.session_state.books.append(book)
  st.success("Добавена книга")
if st.button("покажи книги"):
  if(st.session_state.books) == 0:
    st.write("няма книга")
  else:
    for book in st.session_state.books:
      st.write("заглавие:",book["title"])
      st.write("цена:",book["price"])
      st.write("автор",book["author"])
st.header("по автор")
search = st.text_input("ваведи автор на книгата ")
if st.button("намери"):
  found = False
  for book in st.session_state.books:
    if book["author"] == search :
      st.write(book)
      found == True
    if found == False:
      st.write("Няма такава книга")
