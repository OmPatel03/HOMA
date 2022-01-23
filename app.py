
from nbformat import read
from loadjson import getProblemDictionary
#from speech import *;
#from image_reader import readImage
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

    user_input = st.text_input(
        "Type in or say a business-related mathematical problem and HOMA will attempt to solve it!")
    if st.button("Record speech"):
        st.write("Recording...")
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
        final, variables = compute_word_problem(user_input)
        st.markdown("#### " + final)
        if type(variables) == dict:
            st.markdown("""
                    <style>
                    .big-font {
                        font-size:15px !important;
                        color: #5A6370
                        

                        }
                        </style>
                        """, unsafe_allow_html=True)
            for variable in variables:

                st.markdown("<p class = 'big-font'>" + variable + " : " + "" +
                            str(variables[variable]) + "" + "</p>", unsafe_allow_html=True)
