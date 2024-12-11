import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

# Step 1: Fetch the webpage content
url = "http://books.toscrape.com/catalogue/page-1.html"
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    print("Successfully fetched the webpage.")
else:
    print(f"Failed to fetch the webpage. Status code: {response.status_code}")
    exit()

# Step 2: Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Step 3: Extract book titles and prices
books = soup.find_all('article', class_='product_pod')

# Step 4: Prepare data for Excel
data = [["Title", "Price"]]  # Include headers
for book in books:
    title = book.h3.a['title']  # Extract the book title
    price = book.find('p', class_='price_color').text  # Extract the book price
    data.append([title, price])

# Step 5: Save data to an Excel file
excel_file = "books.xlsx"
workbook = Workbook()
sheet = workbook.active
sheet.title = "Books"

# Write data to the sheet
for row in data:
    sheet.append(row)

# Save the workbook
workbook.save(excel_file)

print(f"Data saved to {excel_file}.")
