"""
Quantiztion table viewer

this is a script that extracts chrominance and luminace quantization tables of an image
then from a list of available tables we can deduce the software used to export the image this can come in handy in cases where
metadata has also been tampered with or is not available.
"""
import streamlit as st
import jpegio as jio 
import start_screen

def app():
    try:
        jpeg = jio.read(start_screen.x)  
        col1, col2 = st.beta_columns(2)
        # coef_array = jpeg.coef_arrays[0]  
        with col1:
            quant_tbluminace = jpeg.quant_tables[0]
            st.write("luminance",quant_tbluminace)
        with col2:
            quant_tbcrominace = jpeg.quant_tables[1]
            st.write("Chrominace",quant_tbcrominace)
                    
        st.write("Matches")
    except AttributeError:
        st.error("no image selected")

    