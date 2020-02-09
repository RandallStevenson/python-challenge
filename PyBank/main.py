import os as os
import csv as csv

input_path=os.path.join("Resources","budget_data.csv")

with open(input_path,'r',newline='') as outfile:

#read file
    bank_data=csv.reader(outfile,delimiter=",")

#initialize variables
    max_pi=0
    max_mo=""
    min_pd=0
    min_mo=""
    tot_pl=0
    header=True
    flag=True

#loop through lines of file reading and acting of each line
    for row in bank_data:
# Input first months data to initiate change determinations using boolian
        if header==True:
            junk=row
            header=False
        elif flag==True:
            prior_pl=int(row[1])
            initial_pl=prior_pl
            tot_pl += prior_pl
            flag=False
            count_pl=1
# Input months after first month
        else:
            pl=int(row[1])
#determine change from prior month
            change=pl-prior_pl
#compute total profits/losses to data
            tot_pl += pl
#increment no of months of data
            count_pl += 1
            if change<min_pd:
                min_pd=change
                min_mo=row[0]
            elif change>max_pi:
                max_pi=change
                max_mo=row[0]
            prior_pl=pl

# open file for output

with open("bank_output.txt","w") as outfile:

# rather than print and write each line, set up a function to that

    def out(note):
        print(note)
        outfile.write(note+"\r")

    out("Financial")
    out("Analysis")
    out("-----------------------------------")
    out("Total Months:  "+str(count_pl))
    out("Total:   $"+str(tot_pl)+"")
# avg of changes in p/l - could actually average changes, but mathematically
# it is the total change per number of months with changes, so simple method used
    out("Average Change:  ($"+str(round((prior_pl-initial_pl)/(count_pl-1)))+")")
# conditioned printing greatest increase on there being an increase
    if max_pi>0:
        out("Greatest Increase in Proftis: "+max_mo+": ($"+str(max_pi)+")")
    else:
        out("There is no month with an increase in profits.")
# conditioned printing greatest decrease on there being a decrease
    if min_pd<0:
        out("Greatest Decrease in Proftis: "+min_mo+": ($"+str(min_pd)+")")
    else:
        out("There is no month with a decrease in profits.")
