from loadjson import getProblemDictionary
#from speech import *;
from image_reader import readImage
import streamlit as st

# Main Loop
if (__name__ == "__main__"):

    st.title("HOMA")
    user_input = st.text_input("Math Problem")

    #
    # Import
    problemDict = getProblemDictionary()

    #
    # Get String from Speech or Image
    file_path = "path of the file we want to read and extract the text from"
    #imageText = readImage(file_path)

    #
    # Decide what type of function the string denotes

    #
    # Seperate the Speech Speach string into it's key variables based on the type of function

    #
    # Exectue the function using the variables

    #
    # Create a stringified version to send back to the person.

    # end
    pass
