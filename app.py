#from speech import *;
from image_reader import readImage
from string_solve import compute_word_problem;


#Main Loop
if (__name__ == "__main__"):

    #
    #Import

    #
    #Get String from Speech or Image
    file_path = "path of the file we want to read and extract the text from"
    imageText = readImage(file_path)

    #
    #Compute
    result = compute_word_problem(imageText)

    #end
    pass
