import streamlit as st
import SessionState

wt = ['initialised text']
ss = SessionState.get(wt=wt)

st.header('Watchlist')

container1 = st.beta_container()
sym = container1.text_input('for adding')
container2 = st.beta_container()
add_button = container2.button('add')

if add_button:
    ss.wt.append(sym)

st.write(ss.wt)
