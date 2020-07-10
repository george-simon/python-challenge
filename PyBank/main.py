#Have to use csv file - take file see what you have (programming the same)
#program doesn't know where file is -> have to tell it.
import os
import csv

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
    for i in revenue:
        print(i)
        #diff_revenue.append(revenue[i] -  revenue[i+1])

        # The greatest increase in profits (date and amount) over the entire period
        #GUESS: DEFINE function and RETURN greatest increase, date, and amount


        # The greatest decrease in losses (date and amount) over the entire period
        #GUESS: DEFINE function and RETURN greatest decrease, date, and amount


    print(f"Financial Analysis \n----------------------------")
    print(f"Number of Months: {len(months)}") #total months or rows counted
    print(f"Net Total: ${sum(revenue)}") #total months or rows counted
    print(f"Average of Change: {diff_revenue}")

 