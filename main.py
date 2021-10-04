# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import altair as alt

def resizeimg(img_path):

    seg = Image.open(img_path)
    img = seg.resize((250, 250), Image.ANTIALIAS)

    return img


st.write("""# Image-Data-driven model by IMM-MFM """)
#st.image("logo.png")
st.markdown('---')
st.write("""
## This web-based interative tool provide a deep-learning-based *image, mechanical* analysis of __Dual phase steel __on the fly.
to use the model, upload the image and select the functionality.
""")
st.markdown('---')



seg = resizeimg("sematic_segmented.png")
crack_pattern_img = resizeimg("fracture_path.PNG")
stress_field_X= resizeimg("stress_field.png")
mesh= resizeimg("Mesh.png")

load_disp_img = Image.open("load_displacement_curve.png")

def user_input_features(seg):

    Inputdata_typ = st.sidebar.selectbox('Input datatyp', ('Image', 'Feature data',))
    if Inputdata_typ == 'Image':

        # Collects user input features into dataframe
        uploaded_file = st.sidebar.file_uploader("Upload your input image file", type=["png"])

        if uploaded_file is not None:

            img = resizeimg(uploaded_file)

            st.write("""This is how your image looks like: """)
            st.image(img)

        else:
            st.warning('Please upload a image.')

    material_typ = st.sidebar.selectbox('Material type',('Dual Phase Steel','None'))


    analysis_typ = st.sidebar.selectbox('Analyis type',('Image analysis','Mechanical analysis',))
    if analysis_typ == 'Image analysis':
        function_ = st.sidebar.selectbox('Functions',('Segmentation','Feature analysis'))
        if function_ == 'Feature analysis':
            feature1 = st.sidebar.checkbox('Feature 1')
            feature2 = st.sidebar.checkbox('Feature 2')
            feature3 = st.sidebar.checkbox('Feature 3')

    elif analysis_typ == 'Mechanical analysis':
        function_ = st.sidebar.selectbox('Functions', ('Mesh Creation','Stress Visualiaztion', 'Crack pattern','Stress-Strain Curve'))
        if function_ == 'Mesh Creation':
            st.write("""Please select the mesh size: """)
            add_slider=st.slider(
                'Select a range of mesh size',
                0.0, 10.0, (2.50, 7.50)
            )



        if analysis_typ == 'Mechanical analysis' and function_ == 'Stress Visualiaztion' or 'Crack pattern' or 'Stress-Strain Curve':

            loading_x = st.sidebar.checkbox('loading - x')
            loading_y = st.sidebar.checkbox('loading - y')
            loading_xy = st.sidebar.checkbox('loading - xy')


    run_ = st.sidebar.button('run analysis')

    if run_ and function_ == 'Segmentation':

        st.markdown('---')
        st.write("""This is your segmented image: """)
        st.image(seg)

    elif run_ and function_ == 'Feature analysis':
        st.markdown('---')
        st.write("""This is the data we could provide:""")


        if feature1:

            df = pd.DataFrame(np.random.randn(200, 3),columns = ['a', 'b', 'c'])
            c = alt.Chart(df).mark_circle().encode(x = 'a', y = 'b', size = 'c', color = 'c', tooltip = ['a', 'b', 'c'])
            st.altair_chart(c, use_container_width=True)

        else:
            st.warning('The current function not available yet, please select another function')


    elif run_ and function_ == 'Crack pattern':

        if loading_x:
            st.markdown('---')
            st.write("""This is the visualization we could provide:""")
            st.image(crack_pattern_img)
        else:
            st.warning('Function not available yet')



    elif run_ and function_ == 'Stress-Strain Curve':
        if loading_x:
            st.markdown('---')
            st.write("""This is the Stress-Strain Curve we could provide:""")
            st.image(load_disp_img)
        else:
            st.warning('Function not available yet')


    elif run_ and function_ == 'Stress Visualiaztion':
        st.markdown('---')
        st.write("""This is the Stress visualization we could provide:""")
        st.image(stress_field_X)

    elif run_ and function_ == 'Mesh Creation':
        st.markdown('---')
        st.write("""This is the Mesh we could provide, you can save the .geo file by clicking the button:""")
        st.image(mesh)
        save_ = st.button('Save mesh')


#st.write("""The function is not available yet""")

    #selc_= st.sidebar.selectbox('Select', [1, 2, 3])

    #bill_length_mm = st.sidebar.slider('Bill length (mm)', 32.1,59.6,43.9)
    #bill_depth_mm = st.sidebar.slider('Bill depth (mm)', 13.1,21.5,17.2)
    #flipper_length_mm = st.sidebar.slider('Flipper length (mm)', 172.0,231.0,201.0)
    #body_mass_g = st.sidebar.slider('Body mass (g)', 2700.0,6300.0,4207.0)
    # data = {'island': analysis_typ
    #         }
    # features = pd.DataFrame(data, index=[0])
    # return features

input_df = user_input_features(seg)


