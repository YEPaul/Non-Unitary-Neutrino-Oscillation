import csv

input_file_name = 'v52.release-SKyes-NO.txt'
output_file_name = 'T13DCP.csv'
start_row = 1347246  # Starting row (1-based indexing)
end_row = 1354691  # Ending row (inclusive)

with open(input_file_name, 'r') as infile, open(output_file_name, 'w', newline='') as outfile:
    reader = csv.reader(infile, delimiter=' ')  # Space as delimiter
    writer = csv.writer(outfile)

    for i, row in enumerate(reader, start=1):
        if start_row <= i <= end_row:
            # Filter out empty strings if there are multiple spaces
            filtered_row = [item for item in row if item]
            writer.writerow(filtered_row)
        elif i > end_row:
            break


