import requests
from bs4 import BeautifulSoup
import csv

# Base URL for the website
base_url = "http://books.toscrape.com/catalogue/page-{}.html"

# Open a CSV file to save the results
csv_file = "books_multiple_pages.csv"
with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Price"])  # Write headers

    # Loop through multiple pages
    for page in range(1, 6):  # Adjust the range based on the number of pages
        print(f"Scraping page {page}...")
        url = base_url.format(page)
        response = requests.get(url)

        # Check if the page exists
        if response.status_code != 200:
            print(f"Page {page} not found. Stopping.")
            break

        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract book details
        books = soup.find_all('article', class_='product_pod')
        for book in books:
            title = book.h3.a['title']  # Extract the book title
            price = book.find('p', class_='price_color').text  # Extract the book price
            writer.writerow([title, price])  # Write to CSV file

print(f"Scraped data saved to {csv_file}.")
