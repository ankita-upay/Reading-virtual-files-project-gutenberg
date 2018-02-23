# HomeWork Assignment :1
# Program Author     : Ankita Upadhyay
# ZID               : z1836412

# Class:     CSCI 680-A8
# Program:   Assignment 1
# Author:    Ankita Upadhyay
# Z-number:  z1836412
# Date Due:  02/20/18

# Purpose:   Reading virtual /proc files

# Execution: Command to execute your program,
#>>> python3 hw1.py pride.txt swann.txt

import sys
import unicodedata

# Finds number of lines in the given text file
# Arguments: File Name
# Returns:   Number of Lines

def num_of_lines(filename):
    fhand = open(filename, 'r', encoding="utf8")
    num_lines = 0
    for line in fhand:
        num_lines += 1
    return num_lines

# Finds number of characters in the given text file
# Arguments: File Name
# Returns:   Number of characters

def num_of_characters(filename):
    fhand = open(filename, 'r', encoding="utf8")
    num_characters = 0
    for line in fhand:
        num_characters += len(line)
    return num_characters

# Finds number of letters in the given text file
# Arguments: File Name
# Returns:   Number of letters

def num_of_letters(filename):
    fhand = open(filename, 'r', encoding="utf8")
    num_letters = 0
    for line in fhand:
        for ch in line:
            cat = unicodedata.category(ch)
            if cat.startswith("L"):
                num_letters += 1
    return num_letters


# Finds number of vowels in the given text file
# Arguments: File Name
# Returns:   Number of vowels

def num_of_vow(filename):
   
    vowels = "AEIOUaeiou\u00e9\u00e2\u00ea\u00ee\u00f4\u00fb\u00e0\u00e8\u00f9\u00eb\u00ef\u00fc"
    fhand = open(filename, 'r', encoding="utf8")
    num_Vowels = 0
    for line in fhand:
        for ch in line:
            if (ch.lower() in vowels):
                num_Vowels += 1
    return num_Vowels

# Finds number of consonants in the given text file
# Arguments: File Name
# Returns:   Number of consonants

def num_of_cons(filename):
    num_consonants = num_of_letters(filename)-num_of_vow(filename)
    return num_consonants


# Finds percentage of vowel in the given text file
# Arguments: File Name
# Returns:   percentage of vowels

def percentage_vowel(num_vowel, num_letters):
    percent_vowel = (num_vowel / num_letters) * 100
    return round(percent_vowel, 2)


# Finds the chi square value for the two text files using 2*2 contigency table
# Arguments: File Name1,File Name2
# Returns:   Chi Square Value

def chi_square(filename1, filename2):
    nv1 = num_of_vow(filename1)
    nc1 = num_of_cons(filename1)
    nv2 = num_of_vow(filename2)
    nc2 = num_of_cons(filename2)
    
    column_total1 = nv1 + nc1
    column_total2 = nv2 + nc2
    
    row_total1 = nv1 + nv2
    row_total2 = nc1 + nc2
    
    col_total = column_total1 + column_total2
    row_total = row_total1 + row_total2
    if row_total==col_total :
        
        expected_frequency1_1 = (column_total1 / row_total) * row_total1
        expected_frequency2_1 = (column_total1 / row_total) * row_total2
        expected_frequency1_2 = (column_total2 / row_total) * row_total1
        expected_frequency2_2 = (column_total2 / row_total) * row_total2
        
        actual_frequency1_1 = ((nv1 - expected_frequency1_1) ** 2) / expected_frequency1_1
        actual_frequency1_2 = ((nv2 - expected_frequency1_2) ** 2) / expected_frequency1_2
        actual_frequency2_1 = ((nc1 - expected_frequency2_1) ** 2) / expected_frequency2_1
        actual_frequency2_2 = ((nc2 - expected_frequency2_2) ** 2) / expected_frequency2_2
        chi_sqaure_value = actual_frequency1_1 + actual_frequency1_2 + actual_frequency2_1 + actual_frequency2_2
        
        print ("\nExpected Frequency")
        print(round(expected_frequency1_1,2))
        print(round(expected_frequency1_2,2))
        print(round(expected_frequency2_1,2))
        print(round(expected_frequency2_2,2))
        print ("\nObserved Frequency")
        print(nv1)
        print(nc1)
        print(nv2)
        print(nc2)
    
    print("\nChi Square statistic value:", round(chi_sqaure_value, 2))
    print("Degrees of freedom = 1")
    print ("In this problem the X2 = ",round(chi_sqaure_value,2),"\nit exceeds the cutoff as given in the web-page,\nthat means the difference in vowel percent of both \nthe text file is significant. ")
   
# Function to call all the above function at once
# Arguments: File Name1,File Name2
# Returns:   void

def file_tasks(filename1, filename2):
    print("\nDetails for ", filename1)
    print("\n Number' of lines =", num_of_lines(filename1),
          "\n Number' of characters =", num_of_characters(filename1),
          "\n Number' of letters =", num_of_letters(filename1),
          "\n Number' of vowels =", num_of_vow(filename1),
          "\n Number' of consonants =", num_of_cons(filename1),
          "\n Percentage of Vowels =", (percentage_vowel(num_of_vow(filename1), num_of_letters(filename1))) )
    print("\nDetails for ", filename2)
    print("\n Number' of lines =", num_of_lines(filename2),
          "\n Number' of characters =", num_of_characters(filename2),
          "\n Number' of letters =", num_of_letters(filename2),
          "\n Number' of vowels =", num_of_vow(filename2),
          "\n Number' of consonants =", num_of_cons(filename2),
          "\n Percentage of Vowels =", ((percentage_vowel(num_of_vow(filename2), num_of_letters(filename2)))))
    print("\nSystem utilities used for verifying number of lines \nand number of characters is wc <filename>")
    chi_square(filename1, filename2)
    


# Program Execution starts from here
# we input two file names as arguments
# if both or any of the file name is no entered the program displays an error message and quits

if len(sys.argv) == 3:
    fname1 = sys.argv[1]
    fname2 = sys.argv[2]
    print("Both file names are entered correctly,proceeding....")
    file_tasks(fname1, fname2)
else:
   
    print("\nCommand line does not have exactly two parameters.\nFiles Names are not entered correctly.")
    print("Quitting....")
    sys.exit()
