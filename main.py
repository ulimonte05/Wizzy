import streamlit as st
import os
from streamlit_chat import message
from streamlit.components.v1 import html
from service.pandasai import generateResponse
import pandas as pd
import google.generativeai as genai

genai.configure(api_key=os.getenv('API_KEY'))

# Cargar el archivo CSV de inventario
df = pd.read_csv("./db/ecommerce_inventory.csv")


def on_input_change():
    user_input = st.session_state.user_input
    st.session_state.past.append(user_input)
    response = generateResponse(user_input)
    st.session_state.generated.append(response)

def on_btn_click():
    del st.session_state.past[:]
    del st.session_state.generated[:]

def show_inventory():
    st.header("Inventario")
    st.dataframe(df)

audio_path = "https://docs.google.com/uc?export=open&id=16QSvoLWNxeqco_Wb2JvzaReSAw5ow6Cl"
img_path = "https://www.groundzeroweb.com/wp-content/uploads/2017/05/Funny-Cat-Memes-11.jpg"
youtube_embed = '''
<iframe width="400" height="215" src="https://www.youtube.com/embed/LMQ5Gauy17k" title="YouTube video player" frameborder="0" allow="accelerometer; encrypted-media;"></iframe>
'''

markdown = """
### HTML in markdown is ~quite~ **unsafe**
<blockquote>
  However, if you are in a trusted environment (you trust the markdown). You can use allow_html props to enable support for html.
</blockquote>

* Lists
* [ ] todo
* [x] done

Math:

Lift($L$) can be determined by Lift Coefficient ($C_L$) like the following
equation.

$$
L = \\frac{1}{2} \\rho v^2 S C_L
$$

~~~py
import streamlit as st

st.write("Python code block")
~~~

~~~js
console.log("Here is some JavaScript code")
~~~

"""

table_markdown = '''
A Table:

| Feature     | Support              |
| ----------: | :------------------- |
| CommonMark  | 100%                 |
| GFM         | 100% w/ `remark-gfm` |
'''

st.session_state.setdefault("past", [])
st.session_state.setdefault("generated", [])

st.title("Wizzy")

# Agregar la selección de sección en la barra lateral
section = st.sidebar.selectbox("Seleccionar sección", ["Chat", "Inventario"])

if section == "Chat":
    chat_placeholder = st.empty()

    with chat_placeholder.container():
        for i in range(len(st.session_state['generated'])):
            message(st.session_state['past'][i], is_user=True, key=f"{i}_user")
            response = generateResponse(st.session_state['generated'][i])
            message(
                response, 
                key=f"{i}", 
                allow_html=True,
            )

        st.button("Clear message", on_click=on_btn_click)

    with st.container():
        st.text_input("User Input:", on_change=on_input_change, key="user_input")
elif section == "Inventario":
    show_inventory()
