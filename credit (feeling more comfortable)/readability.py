# Import the get_string function from the cs50 library
from cs50 import get_string

# Initialize counters to zero
letters = 0  # This counter will keep track of the number of alphabetic characters in the text
sentences = 0  # This counter will count the number of sentences based on punctuation marks
words = 1  # This counter will track the number of words. Initialized to 1 to account for the first word in the text

# Prompt the user to enter a string of text
text = get_string("Text: ")

# Loop through each character in the input text
for i in range(len(text)):
    # Check if the current character is an alphabetical letter
    if text[i].isalpha():
        letters += 1  # If true, increment the letters counter
    # Check if the current character is a space, which typically separates words
    elif text[i] == ' ':
        words += 1  # If true, increment the words counter
    # Check if the current character is one of the sentence-ending punctuation marks (period, exclamation mark, or question mark)
    elif text[i] == '.' or text[i] == '!' or text[i] == '?':
        sentences += 1  # If true, increment the sentences counter

# Calculate the average number of letters per 100 words
Li = (letters / words) * 100
# Calculate the average number of sentences per 100 words
Si = (sentences / words) * 100

# Compute the Coleman-Liau index based on the letter and sentence averages
index = round(0.0588 * Li - 0.296 * Si - 15.8)

# Determine the readability grade level based on the index value
if index > 16:
    # If the index is greater than 16, print "Grade 16+" indicating the text is suitable for high school seniors and beyond
    print("Grade 16+")
elif index <= 1:
    # If the index is 1 or less, print "Before Grade 1" indicating the text is suitable for early readers
    print("Before Grade 1")
else:
    # For index values between 1 and 16, print the corresponding grade level
    print("Grade", index)
