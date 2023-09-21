import csv;

csv_input = '../data/raw_data/Discover/Discover-Statement-20230903.csv';
csv_output = '../data/processed_data/Discover/Cleaned-Discover-Statement-20230903.csv';
csv_columns = [0, 3, 4]

with open(csv_input, 'r') as csv_file:
    csv_reader = csv.reader(csv_file);

    with open(csv_output, 'w', newline='') as new_file:
        csv_writer = csv.writer(new_file);

        for line in csv_reader:
            selected_columns = [line[i] for i in csv_columns]
            csv_writer.writerow(selected_columns);

print(f"The cleaned data has been saved to {csv_output}");