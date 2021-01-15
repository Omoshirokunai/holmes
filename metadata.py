"""
metadata viewer

This script extracts the exif metadata from the image in main.py and displays it in a streamlit dataframe
"""
import streamlit as st  
from skimage.io import imread
import pandas as pd
import exifview
import start_screen



def app():
    try:
        im = str(start_screen.x)
        img = imread(im)
        col1, col2 = st.beta_columns((1,2))
        col1.header("Image")
        col1.image(img, use_column_width=True)
        
        with col2:
            col2.header("Image Metadata")
            p = exifview.exif_meta(im)
            if p:
                df = pd.DataFrame(list(p.items()),columns = ['exif','values'])
                st.dataframe(df,900,500)
            else:
                st.error("Sorry No Exif Found :crying_cat_face:")
    except AttributeError:
        st.error("no image selected")
        
        
    
        