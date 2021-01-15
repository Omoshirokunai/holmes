"""
holmes main script

This the main streamlit script that contains page navigation and image to be processed
"""

import metadata
import quantization_table
import streamlit as st
import ela
import os
import start_screen
import easygui as g
from skimage.io import imread
import pandas as pd
import exifview

# st.set_page_config(page_title='HOLMES', layout = "wide", initial_sidebar_state = 'auto')

PAGES = {
    "welcome": start_screen,
    "EXIF data": metadata,
    "Quantization Tables":quantization_table,
    "Error Level Analysis": ela
}

st.sidebar.title('Navigation')
selection = st.sidebar.selectbox("Go to", list(PAGES.keys()),index=0)

page = PAGES[selection]

if st.sidebar.button("Open Image"):
    start_screen.x = start_screen.browseforimage()


# side bar to load pages
if PAGES[selection]:
    w = st.sidebar.slider("zoom",100,400,300,100,format("",""))
    try:
        img= imread(start_screen.x)
        if PAGES[selection] != start_screen:
            st.sidebar.image(img,width=w)
            st.title("{}".format(selection))
            st.write("\n")
    except:
        pass
    finally:
        page.app()


    


