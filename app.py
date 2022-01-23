<<<<<<< HEAD
from loadjson import getProblemDictionary
#from speech import *;
from image_reader import readImage
import streamlit as st
=======
#from speech import *;
from image_reader import readImage
from string_solve import compute_word_problem;

>>>>>>> ee36c0e07a1883d362fa65407b2c8ae60ffafa1b

# Main Loop
if (__name__ == "__main__"):

    st.title("HOMA")
    user_input = st.text_input("Math Problem")

    #
<<<<<<< HEAD
    # Import
    problemDict = getProblemDictionary()
=======
    #Import
>>>>>>> ee36c0e07a1883d362fa65407b2c8ae60ffafa1b

    #
    # Get String from Speech or Image
    file_path = "path of the file we want to read and extract the text from"
    #imageText = readImage(file_path)

    #
<<<<<<< HEAD
    # Decide what type of function the string denotes

    #
    # Seperate the Speech Speach string into it's key variables based on the type of function

    #
    # Exectue the function using the variables

    #
    # Create a stringified version to send back to the person.
=======
    #Compute
    result = compute_word_problem(imageText)
>>>>>>> ee36c0e07a1883d362fa65407b2c8ae60ffafa1b

    # end
    pass
