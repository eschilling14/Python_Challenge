import os
import csv

votes_cast = 0
candidates = []
win_perc = []
total_wins = 0
winner = []

poll_data = os.path.join("PyPoll" , "election_data.csv")

with open(poll_data, newline="") as csvfile:
    reader = csv.reader(csvfile, delimiter = ",")

    header = next(reader)

    first_row = next(reader)
    votes_cast = votes_cast + 1
print(votes_cast)

