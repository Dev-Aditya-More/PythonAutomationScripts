import requests
from bs4 import BeautifulSoup

# URL of the page you want to scrape
url = 'https://longform.org'  # Replace with the actual URL

# Fetch the content of the page
response = requests.get(url)



# Check if the request was successful
if response.status_code == 200:
    page_content = response.content

    # Parse the HTML content
    soup = BeautifulSoup(page_content, 'html.parser')

    # Find all headings on the page
    headings = soup.find_all(['h1', 'h2', 'h3'])

    # Save the extracted headings to a text file
    with open('headings.txt', 'w') as file:
        for heading in headings:
            file.write(heading.text.strip() + '\n')
else:
    print(f'Failed to retrieve the page: {response.status_code}')


def scrape_pages(base_url, num_pages):
    for page in range(1, num_pages + 1):
        url2 = f"{base_url}?page={page}"  # Modify based on website's pagination structure
        resp = requests.get(url2)

        if resp.status_code == 200:
            soupp = BeautifulSoup(resp.content, 'html.parser')
            # Extract your data here
            headings2 = soupp.find_all(['h1', 'h2', 'h3'])
            # Save or process data as needed
            # ...
        else:
            print(f'Failed to retrieve page {page}: {resp.status_code}')


# Example usage
scrape_pages('https://longform.org/random', 5)  # Scrape the first 5 pages
