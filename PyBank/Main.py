#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Import Modules
import os
import csv


# In[16]:


#Build the path to the csv file
csv_path = os.path.join("Resources","budget_data.csv")

#Open a file handler
with open(csv_path,"r",newline="") as csv_file:
    
    #connect the csv file with a file reader
    csv_reader = csv.reader(csv_file, delimiter=",")
    
    #remove the header
    header = next(csv_reader)
    
    #define counters
    total_months = 0
    total_profit = 0
    first = 0
    first_iteration = True
    
    delta_list = []
    date_list = []
    
    for row in csv_reader:
        
        #Calculate the total months
        total_months += 1
        
        #Calculate total profit
        profit = int(row[1])
        total_profit += profit
        
        #Calculate the change
        second = int(row[1])
        delta = second - first
        
        #Skip the first calculation for delta as it is not a true delta
        if first_iteration == False:
            delta_list.append(delta)
            date_list.append(row[0])
            
        
        
        first_iteration = False
        first = second
        
    #Final Calculations
    max_change = max(delta_list)
    min_change = min(delta_list)
    average_change = round(sum(delta_list)/len(delta_list), 2)
    
    #Identify dates for max and min change
    index = 0
    for index in range(len(delta_list)):
        
        if int(delta_list[index]) == max_change:
            max_index = index
            
            
        if int(delta_list[index]) == min_change:
            min_index = index
            
            
    index += 1
    
max_date = date_list[max_index]
min_date = date_list[min_index]
    
#Print report on terminal
print("Financial Analysis")
print("---------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {max_date} (${max_change})")
print(f"Greatest Decrease in Profits: {min_date} (${min_change})")
    
        
output_file_path = os.path.join("Resources", "output.txt")

with open(output_file_path,"w",newline = "") as output_file:
    
    output_file.write("Financial Analysis\n")
    output_file.write("-------------------------------\n")
    output_file.write("Total Months: " + str(total_months) + "\n")
    output_file.write("Total: $" +str(total_profit) + "\n")
    output_file.write("Average Change: $" + str(average_change) + "\n")
    output_file.write("Greatest Increase in Profits: " + max_date + " ($" + str(max_change) + ")\n")
    output_file.write("Greatest Decrease in Profits: " + min_date + " ($" + str(min_change) + ")\n")


# In[ ]:




