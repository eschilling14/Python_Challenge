import os
import csv


budget_data= os.path.join("..", "PyBank", "budget_data.csv")
with open (budget_data, newline="") as csvfile:
    csvbudgetread= csv.reader(csvfile, 
    delimiter=",")


    print (csvbudgetread)