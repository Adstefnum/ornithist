# import requests
# from bs4 import BeautifulSoup

# url = "https://en.wikipedia.org/wiki/List_of_birds_by_common_name"
# response = requests.get(url)
# soup = BeautifulSoup(response.content, "html.parser")

# elements = soup.find_all("li")

# for element in elements:
#     a_tag = element.find("a")
#     href = a_tag["href"]
#     name = a_tag.text
#     print("Href:", href)
#     print("Name:", name)
import requests
import csv
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/List_of_birds_by_common_name"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

elements = soup.find_all("li")

data = []
for element in elements:
    try:
        a_tag = element.find("a")
        href = "https://wikipedia.org" + a_tag["href"]
        # print(href)
        name = a_tag.text
        # print(name)
        data.append([name, href])
    except:
        pass

# Save data to a CSV file
filename = "output.csv"
with open(filename, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Href"])
    writer.writerows(data)

print("CSV file created successfully!")

