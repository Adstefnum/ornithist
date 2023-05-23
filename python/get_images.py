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

# Update CSV with image links and scientific names
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
            scientific_name = alt_text.replace("-", "").strip()
        else:
            image_link = "N/A"
            scientific_name = "N/A"
    else:
        image_link = "N/A"
        scientific_name = "N/A"

    row.append(image_link)
    row.append(scientific_name)

# Save updated data to a new CSV file
new_filename = "output_with_images.csv"
with open(new_filename, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(header + ["Image Link", "Scientific Name"])
    writer.writerows(data)

print("CSV file updated with image links and scientific names successfully!")
