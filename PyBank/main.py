#Have to use csv file - take file see what you have (programming the same)
#program doesn't know where file is -> have to tell it.
import os
import csv
import statistics

budget_dataPath = os.path.join("Resources","budget_data.csv")

with open(budget_dataPath, newline='') as csvfile :
    reader = csv.reader(csvfile, delimiter=',')
    next(reader, None)  # skip the headers


    # Make calculations total months 
    # Need to count rows (Loop- count, total months | second column Sum)
    months = []
    revenue = []
    diff_revenue = []
    
    for row in reader:
        months.append(row[0])
        revenue.append(int(row[1]))
    

    # average of changes - loop through revenue list, sum, and divide by total months
    #index range code help: https://stackoverflow.com/questions/37619848/python-loop-list-index-out-of-range
    #finding the mean (average): https://stackoverflow.com/questions/9039961/finding-the-average-of-a-list
    for i in range(len(revenue)-1):
        diff_revenue.append(revenue[i] - revenue[i+1])
        print(diff_revenue) #something is not right here?...

        avg_change = statistics.mean(diff_revenue)

        # The greatest increase in profits (date and amount) over the entire period
        #GUESS: DEFINE function and RETURN greatest increase, date, and amount


        # The greatest decrease in losses (date and amount) over the entire period
        #GUESS: DEFINE function and RETURN greatest decrease, date, and amount

#Print out analysis
    print(f"Financial Analysis \n----------------------------")
    print(f"Number of Months: {len(months)}") #total months or rows counted
    print(f"Net Total: ${sum(revenue)}") #total months or rows counted
    print(f"Average of Change: ")

 