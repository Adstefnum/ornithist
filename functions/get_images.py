import requests
import csv
from bs4 import BeautifulSoup

# Read existing CSV file
filename = "output.csv"
new_filename = "output_with_images.csv"
data = []

file = open(filename, "r", encoding="utf-8")
reader = csv.reader(file)
header = next(reader)  # Skip header row
data = list(reader)

file = open(new_filename, "w", newline="", encoding="utf-8")
writer = csv.writer(file)
writer.writerow(header + ["Image Link", "Scientific Name"])

for row in data:
    href = row[1]
    page_response = requests.get(href)
    page_soup = BeautifulSoup(page_response.content, "html.parser")
    a_element = page_soup.find("a", class_="image")

    if a_element:
        image_tag = a_element.find("img")
        if image_tag:
            image_link = "https://en.wikipedia.org" + a_element["href"]
            alt_text = image_tag.get("alt", "")
            scientific_name = alt_text.replace("-", " ").strip()
            scientific_name = scientific_name.replace(".jpg","")
        else:
            image_link = "N/A"
            scientific_name = "N/A"
    else:
        image_link = "N/A"
        scientific_name = "N/A"

    row.append(image_link)
    print(image_link)
    row.append(scientific_name)
    print(scientific_name)

    writer.writerow(row)

print("CSV file updated with image links and scientific names successfully!")
