from bs4 import BeautifulSoup

with open('home.html', 'r') as html_file:
    content = html_file.read()
    #creating an instance of the BeautifulSoup class
    soup = BeautifulSoup(content, 'lxml')
    #print(soup.prettify())
    print(soup.find_all('h1'))
