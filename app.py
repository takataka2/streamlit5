# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-

import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title("Web App")
st.write("**これがstreamlitアプリ**")

img = Image.open("dog.jpg")
st.image(img,width=400)

st.video("https://www.youtube.com/watch?v=DM0bgYFGCIk")

answer = st.button('Say hello')

if answer == True:
     st.write('Why hello there')
else:
     st.write('Goodbye')
    
data = {
    'lat': np.random.randn(100) / 100 + 35.68,
    'lon': np.random.randn(100) / 100 + 139.75,
}
map_data = pd.DataFrame(data)
# 地図に散布図を描く
st.map(map_data)


