import streamlit as st

st.title("Cardápios da Marilu")


tab1, tab2, tab3, tab4 = st.tabs(['Gourmet', 'Cremoso', 'Fruta', 'Sorvete'])

with tab1:

    st.image("img/gourmet.png")

with tab2:

    st.image("img/cremoso.png")

with tab3:

    st.image("img/fruta.png")

with tab4:

    st.image("img/sorvete.png")