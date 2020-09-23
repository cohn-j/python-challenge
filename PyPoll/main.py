#Import modules for path creation and reading of the initial .CSV file.
import os
import csv


#String that is the .CSV path.
election_csv = os.path.join('Resources','election_data.csv')

#Variable to store the total # of votes once the file has been read.
num_votes = 0
#Dictionary to store the candidates and their # of votes.
candidates = {}
#Variable to store the calculation of votes per candidate / total # of votes cast.
percentage = 0.00

with open(election_csv,'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    for row in csvreader:
        #Each iteration of the for loop adds one to the overall vote calculation. Total # of rows excluding the header is the 
        # # of votes of the file contains.
        num_votes += 1
        #determines if row[2] the candidate name is in the dictionary, if not, will add it and also tabulates each iteration to determine
        # the total vote count.
        if row[2] not in candidates:
            candidates[row[2]] = 0
        candidates[row[2]] = candidates[row[2]] + 1  

    # using the list and key functions to split the key (candidate name) away from the dictionary.
    candidates_names = list(candidates.keys())

    # using the list and values functions to split the data point (total vote count) away from the key in the dictionary. 
    candidates_votes = list(candidates.values())
  
    #declare a list to store the %age of votes each candidate received.
    candidates_percentages = []
    #for loop to determine the # of votes each candidate received and then format that calc into a %age.
    for votes in range(len(candidates_votes)):
        percentage = int(candidates_votes[votes]) / num_votes
        percentage = "{:.3%}".format(percentage)
        candidates_percentages.append(percentage)

#print to terminal the results:
print("Election Results")
print("-------------------------")
#for loop goes through the length of the names list and prints an f string combining the name, the %age of votes received
# and the # of votes received.
for row in range(len(candidates_names)):
    print(f"{candidates_names[row]}: {candidates_percentages[row]} ({candidates_votes[row]})")
print("-------------------------")
#using built-in max function to determine the highest value and print the corresponding key (candidate's name).
print(f"Winner: {max(candidates,key=candidates.get)}")
print("-------------------------")            

#writes the analysis to a .txt file. The "\n" is to drop each result to a new line to make the results more visually appealing.
analysis_txt = os.path.join('Analysis','analysis.txt')
with open(analysis_txt,'w') as txtfile:

    txtfile.write("Election Results \n")
    txtfile.write("------------------------- \n")
    for row in range(len(candidates_names)):
        txtfile.write(f"{candidates_names[row]}: {candidates_percentages[row]} ({candidates_votes[row]}) \n")
    txtfile.write("------------------------- \n")
    txtfile.write(f"Winner: {max(candidates,key=candidates.get)} \n")
    txtfile.write("------------------------- \n")    