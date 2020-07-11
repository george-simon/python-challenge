#Start by pulling the csv file in and read
import os
import csv

election_dataPath = os.path.join("Resources","election_data.csv")

with open(election_dataPath, newline='') as csvfile :
    reader = csv.reader(csvfile, delimiter=',')
    next(reader, None)  # skip the headers

    # The total number of votes cast - create loop and sum
    votes = []
    Khan = 0
    OTooley = 0
    Li = 0
    Correy = 0

    for row in reader:
        votes.append(row[2])
        
        if row[2] == "Khan":
            Khan += 1
        elif row[2] == "O'Tooley":
            OTooley += 1
        elif row[2] == "Li":
            Li += 1
        elif row[2] == "Correy":
            Correy += 1
        else:
            pass
        

    
    # A complete list of candidates who received votes
    unique_canadits = set(votes)
    print(unique_canadits)
    # number_unique_canadits = len(unique_canadits)
    # print(number_unique_canadits)

    # The percentage of votes each candidate won
    percentage_K = (Khan / len(votes)) *100
    percentage_O = (OTooley / len(votes)) *100
    percentage_L = (Li / len(votes)) *100
    percentage_C = (Correy / len(votes)) *100

    # The winner of the election based on popular vote.

    #Print Output
    print(f"Election Results \n----------------------------")
    print(f"Total Votes: {len(votes)}")
    print(f"\n----------------------------")
    
    # Print The total number of votes each candidate won & percentage
    print(f"Khan: {round(percentage_K,2)}% {Khan}")
    print(f"O'Tooley: {round(percentage_O,2)}% {OTooley}")
    print(f"Li: {round(percentage_L,2)}% {Li}")
    print(f"Correy: {round(percentage_C,2)}% {Correy}")
