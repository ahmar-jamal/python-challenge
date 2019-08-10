#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import csv


# In[6]:


file_path = os.path.join("Resources","election_data.csv")

with open(file_path, "r", newline = "") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ",")
    
    #Remove header record
    header = next(csv_reader)
    
    #Define Variables and Counters
    total_votes = 0
    
    total_khan = 0
    total_correy = 0
    total_li = 0
    total_tooley = 0
    
    #Calculate Totals
    for row in csv_reader:
        total_votes += 1
        
        if row[2] == "Khan":
            total_khan += 1
        if row[2] == "Correy":
            total_correy += 1
        if row[2] == "Li":
            total_li += 1
        if row[2] == "O'Tooley":
            total_tooley += 1
            
    #Calculate percentat wins
    khan_perc = round(((total_khan/total_votes)*100), 3)
    correy_perc = round(((total_correy/total_votes)*100), 3)
    li_perc = round(((total_li/total_votes)*100), 3)
    tooley_perc = round(((total_tooley/total_votes)*100), 3)
    
    #Set a winner as a counter logic
    winner = "Tooley"
    win_votes = total_tooley
    
    #Identify Winner
    if total_khan > win_votes:
        winner = "Khan"
        win_votes = total_khan
    if total_li > win_votes:
        winner = "Li"
        win_votes = total_li
    if total_correy > win_votes:
        winner = "Correy"
        win_votes = total_correy
        
    
            
    print("Election Results")
    print("-----------------------------")
    print(f"Total Votes: {total_votes}")
    print("-----------------------------")
    print(f"Khan: {khan_perc}% ({total_khan})")
    print(f"Correy: {correy_perc}% ({total_correy})")
    print(f"Li: {li_perc}% ({total_li})")
    print(f"O'Tooley: {tooley_perc}% ({total_tooley})")
    print("-----------------------------")
    print(f"Winner: {winner}")
    print("-----------------------------")
    
    
output_path = os.path.join("Resources","output.txt")
with open (output_path, "w", newline = "\n") as out_file:
    
    out_file.write("Election Results\n")
    out_file.write("-----------------------------\n")
    out_file.write("Total Votes: " + str(total_votes) + "\n")
    out_file.write("-----------------------------\n")
    out_file.write("Khan: " + str(khan_perc) + "%" + " (" + str(total_khan) + ")\n")
    out_file.write("Correy: " + str(correy_perc) + "%" + " (" + str(total_correy) + ")\n")
    out_file.write("Li: " + str(li_perc) + "%" + " (" + str(total_li) + ")\n")
    out_file.write("O'Tooley: " + str(tooley_perc) + "%" + " (" + str(total_tooley) + ")\n")
    out_file.write("-----------------------------\n")
    out_file.write("Winner: " + winner + "\n")
    out_file.write("-----------------------------\n")
    
    


# In[ ]:




