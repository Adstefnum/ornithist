import requests
import csv
from bs4 import BeautifulSoup

# Read existing CSV file
filename = "output.csv"
data = []
with open(filename, "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    header = next(reader)  # Skip header row
    data = list(reader)

# Update CSV with image links
for row in data:
    href = row[1]
    page_response = requests.get(href)
    page_soup = BeautifulSoup(page_response.content, "html.parser")
    image_element = page_soup.find("img", xpath="/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/table/tbody/tr[2]/td/a/img")

    if image_element:
        image_link = image_element["src"]
        alt_text = image_element.get("alt", "")
        scientific_name = alt_text.replace("-", "").strip()
    else:
        image_link = "N/A"
        scientific_name = "N/A"

    row.append(image_link)
    print(image_link)
    row.append(scientific_name)
    print(scientific_name)

# Save updated data to a new CSV file
new_filename = "output_with_images.csv"
with open(new_filename, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(header + ["Image Link", "Scientific Name"])
    writer.writerows(data)

print("CSV file updated with image links successfully!")
