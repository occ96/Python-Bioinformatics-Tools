# Purpose: To count the total sequence length
# Prompt user for input of sequences
seq_input = input("Enter seuqence list: ")
# Create an array that is separated by whitespace
seq_arr = seq_input.split("  ")

# Counter initialized
count = 0
# For loop to get seq sum length
for seq_len in seq_arr:
    # Continue to add tothe growing count
    count = count + int(seq_len)
# Calculate the average
average = count/len(seq_arr)

# Print average seq length
print("The average sequence length is ", average)
