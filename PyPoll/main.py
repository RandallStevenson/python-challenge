# initialize imports
import os
import csv

poll_candidates=[]
no_votes=[]

input_path=os.path.join("Resources","election_data.csv")

with open(input_path,'r',newline='') as poll_file:
    poll_data=csv.reader(poll_file,delimiter=",")

# read header so it does not impact vote data
    header= next(poll_data)

# for each line in the csv file after the header capture the name of the candidatee
    for row in poll_data:
        cand_name=row[2]

# if the candidate is in the list add a vote to the candidate's total,
# if not, add the candidate to the list and set vote count to 1

        if cand_name in poll_candidates:
             no_votes[poll_candidates.index(cand_name)] +=1
        else:
            poll_candidates.append(cand_name)
            no_votes.append(1)

# create a divider for the printed information
space_bar="\n------------------------------------ \n"

#create output file

with open("ElectionResults.txt","w") as outfile:

# print number of candidates and add to file
    line=f"\nNumber of Candidates: {len(poll_candidates)}"
    print(line)
    outfile.write(line+"\n")
    print(space_bar)
    outfile.write(space_bar+"\n")

# print total votes

    tot_vote=sum(no_votes)
    line=f"Total Number of Voters: {tot_vote}"
    print(line)
    outfile.write(line+"\n")
    print(space_bar)
    outfile.write(space_bar+"\n")

#loop through candidates and print their results
    for index in range(len(poll_candidates)):
        percent=round(100*no_votes[index]/tot_vote,2)
        line=f"{percent:5}%    {poll_candidates[index]:12}  ({no_votes[index]:7})"
        print(line)
        outfile.write(line+"\n")


# output winner information. Note: the first name will be printed if there is a tie.
    print(space_bar)
    outfile.write(space_bar+"\n")
    line=f"Winner: {poll_candidates[no_votes.index(max(no_votes))]} ({max(no_votes)})"
    print(line)
    outfile.write(line+"\n")

