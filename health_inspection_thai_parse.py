import csv
import operator

#open the csv file
with open('Inspection_Results.csv','r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)

#write a new file using data from the csv file
    with open('parsed_thai_restaurants.csv', 'w', newline='') as new_file:
        csv_writer = csv.writer(new_file)

#loop function for CSV file
        for line in csv_reader:
            #filter out critical flag
            if line[12] == "Critical": continue
            #filter by cuisine type
            if line[7] == "Thai":
                #filter by rating
                if line[14] == "A":
                    #write line
                    csv_writer.writerow(line[1:16])
                elif line [14] == "B":
                    csv_writer.writerow(line[1:16])
