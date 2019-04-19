# Small Python Scraper 
import requests
from bs4 import BeautifulSoup
from csv import writer

response = requests.get('https://learntocodewith.me/blog/')

soup = BeautifulSoup(response.text, 'html.parser')

posts = soup.find_all(class_='post-title')

# Store website data in csv file
with open('bloginfocodewithme.csv', 'w') as csv_file:
    csv_writer = writer(csv_file)
# csv header
    headers = ['Title', 'Link', 'Date']
    csv_writer.writerow(headers)
    for post in posts:
        title = post.find(class_='h1').get_text().replace('\n','')
# get title and links
        link = post.find('a')['href']
# get date
        date = post.select('time')[0].get_text()
        csv_writer.writerow([title, link, date])




