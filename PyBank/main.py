import os
import csv

month_count = 0
date_list = []
profit_l_list = []
total_p_l = float(0)
change_value_list = []
prior_value = float(0)

csvpath = os.path.join('..','Resources', 'budget_data.csv')

with open(csvpath, 'r',newline='') as csvfile:

    csv_reader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csv_reader)

    for value in csv_reader:
        month_count +=1
        date_list.append(str(value[0]))
        profit_l_list.append(float(value[1]))

        current_value = value[1]
        change_value = float(current_value) - float(prior_value)
        change_value_list.appead(change_value)
        prior_value = current_value
    
def average(change_value_list):
    x = len(change_value_list)
    total = sum(change_value_list) - change_value_list[0]
    avg = total / (x-1)
    return avg

# compute the average change using the created function

average_change = round(average(change_value_list), 2)

# compute total profit/loss for the entire time frame under being analyzed

total_p_l = round(sum(profit_l_list))


# match the dates with the highest and lowest profit/loss values

highest_p_l = round(max(profit_l_list))
lowest_p_l = round(min(profit_l_list))
highest_index = profit_l_list.index(highest_p_l)
lowest_index = profit_l_list.index(lowest_p_l)

# use values list as an index to map to the right date for the highest and lowest profit values

# print report to terminal screen   

print("Financial Analysis")
print("------------------------------")
print(f"Total Months: {month_count}")
print(f"Total: ${total_p_l}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {date_list[highest_index]} ({highest_p_l})")
print(f"Greatest Decrease in Profits: {date_list[lowest_index]} ({lowest_p_l})")

# create a path to a text file in the Output folder

output_path = os.path.join("..", "Output", "Financial_Analysis.txt")
with open(output_path, 'w', newline='') as text_file:

# write the report into a text file in the Output folder

    print("Financial Analysis", file=text_file)
    print('-----------------------------', file=text_file)
    print(f"Total Months: {month_count}", file=text_file)
    print(f"Total: ${total_p_l}", file=text_file)
    print(f"Average Change: ${average_change}", file=text_file)
    print(f"Greatest Increase in Profits: {date_list[highest_index]} ({highest_p_l})", file=text_file)
    print(f"Greatest Decrease in Profits: {date_list[lowest_index]} ({lowest_p_l})",file=text_file)

# close the file written to

    csvfile.close()
