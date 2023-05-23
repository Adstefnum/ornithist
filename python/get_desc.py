import requests
import csv
from bs4 import BeautifulSoup

# Read the CSV file
filename = "output.csv"  # Replace with the path to your CSV file
output_filename = "output_desc.csv"  # Replace with the desired output file name

with open(filename, "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    header = next(reader)  # Skip header row

    # Create a new CSV file for output
    with open(output_filename, "w", newline="", encoding="utf-8") as output_file:
        writer = csv.writer(output_file)
        writer.writerow(header + ["Description"])  # Add a new column header

        for row in reader:
            url = row[1]  # Assuming the URL is in the second column
            response = requests.get(url)
            soup = BeautifulSoup(response.content, "html.parser")

            element = soup.find("p", xpath="/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/p[2]")

            if element:
                description = element.text.strip()
                words = description.split()
                if len(words) > 25:
                    description = ' '.join(words[:25]) + '...'  # Truncate to 25 words

                row.append(description)  # Add the description to the row
            else:
                row.append("Element not found.")  # Add a message if the element is not found

            writer.writerow(row)  # Write the updated row to the output file

print("Descriptions written to the CSV file successfully!")
