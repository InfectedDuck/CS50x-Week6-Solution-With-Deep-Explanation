import csv
import sys


def main():
    # TODO: Check for command-line usage
    if len(sys.argv)!=3:
        print("Usage: python dna.py csvfile sequencetxtfile")

    # variables
    csvfile=sys.argv[1]
    txtfile=sys.argv[2]
    person_DNA_sequences=[]
    DNA_sequences=[]
    longest_matches=[]

    # TODO: Read database file into a variable
    with open(csvfile,mode='r',newline='') as file_csv:
        reader=csv.reader(file_csv)
        DNA_sequences=next(reader)
        for row in reader:
            person_DNA_sequences.append(row)
    DNA_sequences=DNA_sequences[1:]

    # TODO: Read DNA sequence file into a variable
    with open(txtfile,mode='r') as file_txt:
        sequence=file_txt.read().strip()

    # TODO: Find longest match of each STR in DNA sequence
    for subsequence in DNA_sequences:
        longest_matches.append(longest_match(sequence,subsequence))
    match_found=False
    # TODO: Check database for matching profiles
    for j in range(len(person_DNA_sequences)):
        count=0
        for i in range(1,len(person_DNA_sequences[j])):
            if int(person_DNA_sequences[j][i])==longest_matches[i-1]:
                count+=1
        if count == len(person_DNA_sequences[j]) - 1:
            print(person_DNA_sequences[j][0])
            match_found = True
    if not match_found:
        print("No match")


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
