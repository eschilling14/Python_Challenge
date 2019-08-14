import csv
import os
file_to_load = os.path.join("..", "PyPoll" , "election_data.csv")
output_file = os.path.join("pypoll_homework.txt")
total_votes = 0
candidates = []
candidate_won = {}
Winner = ""
winning_count = 0
with open(file_to_load) as election_data:
   reader = csv.reader(election_data)
   header = next(reader)
   for row in reader:
       total_votes = total_votes + 1
       candidate_name = row[2]
       if candidate_name not in candidates:
           candidates.append(candidate_name)
           candidate_won[candidate_name] = 0
       candidate_won[candidate_name] = candidate_won[candidate_name] + 1
winner_votes = {"Khan":2218231,
               "Correy":704200,
               "Li":492940,
               "O'Tooley":105630
               }
final = (
    f"\nElection Results\n"
    f"------------------------\n"
    f"Total Votes: {total_votes}\n"
    f"----------------------------\n"
    f"{candidate_won}\n"
    f"------------------------\n"
    f"Winner: {max(zip(winner_votes.values(), winner_votes.keys()))}\n"
)
print(winner_votes)
print(final)
with open(output_file, "w") as text_file:
   text_file.write(final)
   

