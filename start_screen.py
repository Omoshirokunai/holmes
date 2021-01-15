import os
import easygui as g
import streamlit as st
from PIL import Image
currdir = os.getcwd()
title = 'Choose your image'

def browseforimage():
    valid_images=[".png",".jpg",".bmp"]
    while True:
        try:
            filename = g.fileopenbox(title="pick image",filetypes=[['.png',".jpg",".bmp","Images"]], default = currdir)
            
            if filename[-4:] in valid_images:
                print("file: %s" % filename)
                return filename
            else:
                raise Exception("input a valid image")
        except (TypeError,AttributeError):
            print("Please select a valid image")
            break
        except Exception as e:
            print(e)
            break
        else:
            break
        

def app():
    
    st.title("Welcome :smiley_cat:")
    if(st.button("Open an Image")):
        global x ## lord forgive me for i have sinned
        x = browseforimage()
    try:
        img = Image.open(x)
        col1,col2 = st.beta_columns((1,2))
        with col1:
            st.image(img,use_column_width=True,use_column_height=True)
        with col2:
            st.write(x)
    except (NameError,AttributeError):
        st.info("Images must be in ('jpg','png', or '.bmp') formats")

    