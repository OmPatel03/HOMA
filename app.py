
from cv2 import computeCorrespondEpilines
from loadjson import getProblemDictionary
#from speech import *;
from image_reader import readImage
import streamlit as st
from speech import *
from string_solve import *


def get_speech():
    run()
    with open("text.txt", "r") as f:
        msg = f.read()

    return msg


# Main Loop
if (__name__ == "__main__"):
    st.title("HOMA")
    col1, col2 = st.columns(2)

    with col1:
        user_input = st.text_input("Math Problem")
    with col2:
        if st.button("Record speech"):
            user_input = get_speech()

    #
    # Import
    problemDict = getProblemDictionary()

    #
    # Get String from Speech or Image
    file_path = "text.txt"
    #imageText = readImage(file_path)

    #
    # Decide what type of function the string denotes

    #
    # Seperate the Speech Speach string into it's key variables based on the type of function

    #
    # Exectue the function using the variables

    #
    # Create a stringified version to send back to the person.

    if user_input:
        st.markdown("#### " + compute_word_problem(user_input))
