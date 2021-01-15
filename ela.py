"""
error level analysis

script that displays the output of ela on an image gotten from holmes.py
"""

from PIL import Image, ImageChops, ImageEnhance
import sys, os.path
import start_screen
import streamlit as st


def convert_to_ela_image(path, quality):
    filename = path
    resaved_filename = filename.split('.')[0] + '.resaved.jpg'
    ELA_filename = filename.split('.')[0] + '.ela.png'
    
    im = Image.open(filename).convert('RGB')
    im.save(resaved_filename, 'JPEG', quality=quality)
    resaved_im = Image.open(resaved_filename)
    
    ela_im = ImageChops.difference(resaved_im,im)
    
    extrema = ela_im.getextrema()
    max_diff = max([ex[1] for ex in extrema])
    if max_diff == 0:
        max_diff = 1
    scale = 255.0 / max_diff
    
    ela_im = ImageEnhance.Brightness(ela_im).enhance(scale)
    
    return ela_im

def app():
    try:
        col1, col2 = st.beta_columns((1,2))
        with col1:
            value = st.slider("quality",1,255,95)
            
            p = convert_to_ela_image(start_screen.x,value)
            # p = convert_to_ela_image(metadata.im,value)
            extrema = p.getextrema()
            max_diff = max([ex[1] for ex in extrema])
            st.write("Maximum difference was %d" % (max_diff))
        with col2:
            st.image(p,use_column_width=True)
    except AttributeError:
        st.error("no image selected")
        