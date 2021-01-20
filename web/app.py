# Importing required libraries, obviously
import streamlit as st
import cv2
from PIL import Image
import numpy as np
import os

def about():
	st.write(
		'''
		** This assignment focused on classifying and localizing of bread with the use of Machine learning. 
		DRBox is used for detection of tasks when objects are oriented arbitrarily. This algorithm is used to detect vehicled, ships and airplanes in remote sensing images. But in this case it is used to detect several bread positions.**

		Something about the algorithm here.



Read more :point_right: 
		''')

img = Image.open('Dero.jpg')
st. image (img, use_column_width = True )

def main():
	
    st.title("Bread Detection App :bread: ")
    st.write("**Detector of rotatable bounding boxes implementation in keras and tenserflow.**")

    activities = ["Home", "About"]
    choice = st.sidebar.selectbox("Pick something fun", activities)

    if choice == "Home":

    	st.write("Go to the About section from the sidebar to learn more about it.")
        
        # You can specify more file types below if you want
    	image_file = st.file_uploader("Upload image", type=['jpeg', 'png', 'jpg', 'webp'])

    	if image_file is not None:

    		image = Image.open(image_file)

    		if st.button("Process"):
                
                # result_img is the image with rectangle drawn on it (in case there are faces detected)
                # result_faces is the array with co-ordinates of bounding box(es)
    			result_img, result_faces = detect(image=image)
    			st.image(result_img, use_column_width = True)
    			st.success("Found {} faces\n".format(len(result_faces)))

    elif choice == "About":
    	about()




if __name__ == "__main__":
    main()
