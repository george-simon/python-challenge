#Start by pulling the csv file in and read
import os
import csv

election_dataPath = os.path.join("Resources","election_data.csv")

with open(election_dataPath, newline='') as csvfile :
    reader = csv.reader(csvfile, delimiter=',')
    next(reader, None)  # skip the headers

    # The total number of votes cast - create loop and sum
    votes = []

    for row in reader:
        votes.append(int(row[0]))

    
    # A complete list of candidates who received votes


    # The percentage of votes each candidate won


    # The total number of votes each candidate won


    # The winner of the election based on popular vote.

    #Print Output
    print(f"Election Results \n----------------------------")
    print(f"Total Votes: {len(votes)}")
    print(f"\n----------------------------")