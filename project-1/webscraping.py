#pov: create a program for scrape the data from freelancer.com website and collect 200 entries

import pandas as pd
import requests
from bs4 import BeautifulSoup

Job_Prices = []
Job_Description = []
Job_Skills = []
Job_Bids = []
Job_Verified = []
Job_Days = []

# Iterate through 4 pages and collect 50 entries per page
for page in range(1, 5):
    # Iterate through 50 entries for each  page
    for entry in range(0, 50):
        url = f"https://www.freelancer.com/jobs?page={page}&entry={entry}"
        r = requests.get(url)
        soup = BeautifulSoup(r.text, "lxml")

        # Extract prices
        prices = soup.find_all("div", class_="JobSearchCard-primary-price")
        for price in prices:
            name = price.text.strip()
            if not name:
                name = "/"
            Job_Prices.append(name)

        # Extract descriptions
        descriptions = soup.find_all("p", class_="JobSearchCard-primary-description")
        for desc in descriptions:
            name = desc.text.strip()
            if not name:
                name = "/"
            Job_Description.append(name)

        # Extract skills
        skills = soup.find_all("div", class_="JobSearchCard-primary-tags")
        for skill in skills:
            name = skill.text.strip()
            if not name:
                name = "/"
            Job_Skills.append(name)

        # Extract bids
        bids = soup.find_all("div", class_="JobSearchCard-secondary-entry")
        for bid in bids:
            name = bid.text.strip()
            if not name:
                name = "/"
            Job_Bids.append(name)

        # Extract verified status
        verified = soup.find_all("div", class_="JobSearchCard-primary-heading-status Tooltip--top")
        for status in verified:
            name = status.text.strip()
            if not name:
                name = "/"
            Job_Verified.append(name)

        # Extract days posted
        days = soup.find_all("span", class_="JobSearchCard-primary-heading-days")
        for day in days:
            name = day.text.strip()
            if not name:
                name = "/"
            Job_Days.append(name)

        # Stop the datascraping if 200 entries are collected
        if len(Job_Bids) >= 200:
            break

    
    # Print the extracted data
print(Job_Prices)
print(len(Job_Prices))

print(Job_Description)
print(len(Job_Description))
# print(type(Job_Description[0]))

print(Job_Skills)
print(len(Job_Skills))
# print(type(Job_Skills[0]))

print(Job_Bids)
print(len(Job_Bids))

print(Job_Verified)
print(len(Job_Verified))

print(Job_Days)
print(len(Job_Days))
# print(type(Job_Days[0]))

# Ensure the lists have the same length
max_len = max(len(Job_Prices), len(Job_Description), len(Job_Skills), len(Job_Bids), len(Job_Verified), len(Job_Days))
Job_Prices += ['/' for _ in range(max_len - len(Job_Prices))]
Job_Description += ['/' for _ in range(max_len - len(Job_Description))]
Job_Skills += ['/' for _ in range(max_len - len(Job_Skills))]
Job_Bids += ['/' for _ in range(max_len - len(Job_Bids))]
Job_Verified += ['/' for _ in range(max_len - len(Job_Verified))]
Job_Days += ['/' for _ in range(max_len - len(Job_Days))]

# Create a DataFrame
data = {
    "Price": Job_Prices,
    "Description": Job_Description,
    "Skills": Job_Skills,
    "Bids": Job_Bids,
    "Verified": Job_Verified,
    "Days": Job_Days,
}
df = pd.DataFrame(data)

# Print the DataFrame
print(df)

#convert the dataframe into csv
df.to_csv("C:/Users/user/Desktop/Excel2 dataWeb_scraps.csv")
