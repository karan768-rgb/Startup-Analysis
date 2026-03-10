import streamlit as st
import pandas as pd
import time


st.title('Startup Dashboard')
st.header('i am learning streamlit ')
st.subheader('i am loving it! ')

st.write('this is streamlit app')

st.markdown("""
### My favourite movies
- Inception
- Ninja turtle
- Avengers
""")

st.code("""
def foo(input):
    return input**2
x =foo(2)    
""")

df = pd.DataFrame({
    'name':['karan','dheeraj','vineet'],
    'marks':[100,100,100],
    'Package':[10,12,13]
})
st.dataframe(df)

st.metric('Revenue','Rs 3L','3%')

st.json({
    'name':['karan','dheeraj','vineet'],
    'marks':[100,100,100],
    'Package':[10,12,13]
})

#st.image('IMG-20260217-WA0067.jpg')

st.sidebar.title('Menu')

col1, col2 = st.columns(2)
with col1:
    st.image('IMG-20260217-WA0067.jpg')
with col2:
    st.image('IMG-20260217-WA0067.jpg')

bar = st.progress(0)
for i in range(0,101):
    #time.sleep(0.1)
    bar.progress(i)

email = st.text_input('Enter your email')
password = st.text_input('Enter your password')
#st.date_input('Enter your date')
gender = st.selectbox('Select gender',['Male','Female','others'])

btn = st.button('Login')
if btn:
    if email == "karan@123" and password == "1234":
        st.balloons()
        st.write(gender)
    else:
        st.error('Login Failed')
