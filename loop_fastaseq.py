# Define method for looping over characters in list, FASTA file, or sequence
def method(sequence_access):
    bases = " "
    # For loop to iterate over each character
    for elem in sequence_access:
    # If element is "ATCG" then we can append to growing list
        if (elem.upper() in "ATCG"):
            # Convert to uppercase form
            bases = elem.upper()
    # Return result value
    return bases

# Open the files to use included from the question prompt
sequence_files = open("sequences.txt", "r")
acc = open("AccessionNumbers.txt", "r")

# Readline() alows us to read each line individually
sequence = sequence_files.readline()
access_num= acc.readline()

# Create a while loop to iterate over sequence
while (sequence and access_num):
    # Call function method while removing special characters
    seq_format = method(sequence.strip())
    # REmove any unnecessary characters
    accession_num = access_num.strip()

    # Write to file
    access_output = open(accession_num + ".txt", "w")
    # Write to output file the accession num and seq
    # FASTA format uses ">"
    access_output.write(">" + accession_num)
    access_output.write(sequence)
    access_output.close()
    # Continue to loop through sequences
    seq_format = sequence.readline()
    accession_num = acc.readline()

sequence_files.close()
acc.close()
