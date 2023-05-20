from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text

soup = BeautifulSoup(html_text, 'lxml')

job = soup.find('li', class_ = 'clearfix job-bx wht-shd-bx')

comp_name = job.find('h3', class_ = 'joblist-comp-name').text.replace(' ', '')

skills = job.find('span', class_ = 'srp-skills').text.replace(' ', '')

print(f'''
Company Name: {comp_name}
Required Skills: {skills}
''')


""" with open('home.html', 'r') as html_file:
    content = html_file.read()
    #creating an instance of the BeautifulSoup class
    soup = BeautifulSoup(content, 'lxml')
    #print(soup.prettify())
         h1_tags = soup.find_all('h1')
    #iterating through the list of h1 tags
    for h1 in h1_tags:
        print(h1.text)
    intro_info = soup.find_all('div', class_ = "intro")
    for intro in intro_info:
        intro_heading = intro.h2.text
        #printing the last element of the list
        intro_para = intro.span.text.split()[-1]

        print(intro_heading)
        print(intro_para)  
 """