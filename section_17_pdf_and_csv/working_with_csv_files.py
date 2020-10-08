
import csv

# steps:
# open the file
# csv.reader
# reformat it into a python object list of lists

# open the file
data = open("example.csv", encoding="utf-8")
# csv.reader
csv_data = csv.reader(data)
# reformat it into a python object
data_lines = list(csv_data)

# # view data
# for line in data_lines[:5]:
# 	print(line)


# # get full names
# full_names = []
# for line in data_lines[1:]:
# 	full_names.append(line[1] + " " + line[2])
# print(full_names[1:5])

# writing files
file_to_output = open('to_save_file.csv', mode='w', newline='')
csv_writer = csv.writer(file_to_output, delimiter=',')
csv_writer.writerow(['a','b','c'])

# see documentation for writing data to files
# check out different modes for writing/reading/appending etc.

file_to_output.close()