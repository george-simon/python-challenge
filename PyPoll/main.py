#Start by pulling the csv file in and read
import os
import csv

election_dataPath = os.path.join("Resources","election_data.csv")

with open(election_dataPath, newline='') as csvfile :
    reader = csv.reader(csvfile, delimiter=',')
    next(reader, None)  # skip the headers

    # The total number of votes cast - create loop and sum
    #
    votes = []
    vote_counter = {}

    #loop through data
    for row in reader:
        votes.append(row[2])
        
    #counting items in a list by inputting into a dictionary: https://stackoverflow.com/questions/3496518/using-a-dictionary-to-count-the-items-in-a-list
    #.get method: https://stackoverflow.com/questions/2068349/understanding-get-method-in-python
    for i in votes:
        vote_counter[i] = vote_counter.get(i, 0) + 1

     # A complete list of candidates who received votes   
    print(vote_counter)  


    #calculate percentages
    percentage_K = (vote_counter.get("Khan") / len(votes)) *100
    percentage_O = (vote_counter.get("Correy") / len(votes)) *100
    percentage_L = (vote_counter.get("Li") / len(votes)) *100
    percentage_C = (vote_counter.get("O'Tooley") / len(votes)) *100

    #Print Output
    print(f"Election Results \n----------------------------")
    print(f"Total Votes: {len(votes)}")
    print(f"\n----------------------------")
    
    # Print The total number of votes each candidate won & percentage
    print(f"Khan: {round(percentage_K,2)}% {vote_counter.get('Khan')}")
    print(f"Correy: {round(percentage_O,2)}% {vote_counter.get('Correy')}")
    print(f"Li: {round(percentage_L,2)}% {vote_counter.get('Li')}")
    # print(f""O'Tooley: {round(percentage_C,2)}% {vote_counter.get("O'Tooley")}"")

    # The winner of the election based on popular vote.
    #extract the winner with the most votes out of the dictionary
    #https://stackoverflow.com/questions/268272/getting-key-with-maximum-value-in-dictionary
        #  a) create a list of the dict's keys and values; 
        #  b) return the key with the max value"""  
    v=list(vote_counter.values())
    k=list(vote_counter.keys())
    print(f"The winner is: {k[v.index(max(v))]}")

