from bs4 import BeautifulSoup
import scraper, re

# Erase what's currently on email.html with basic outline to edit
html_del = open('email.html', 'w+')
html_del.write('<!DOCTYPE html>\n<html lang="en">\n<body>\n\n</body>\n</html>')
html_del.close()

html = open('email.html').read()
soup = BeautifulSoup(html, features='html.parser')

def new_tags(hid, message): # Default for creating new tags in html
    new_h2 = soup.new_tag('h2', id=f'{hid}')
    new_h2.string = f'{message}'

    soup.body.append(new_h2)

def wordofday():
    new_tags('wotd', 'Word of the Day')

    scraped = f'{scraper.wotd()[0]}: {scraper.wotd()[1]}'
    new_p = soup.new_tag('p')
    new_p.string = scraped
    soup.body.append(new_p)
wordofday()

def quickeducation(): # Short educational YouTube video
    new_tags('qe', 'Quick Education')
    
    scraped = scraper.qe()
    new_a = soup.new_tag(f'a href={scraped[1]}')
    new_a.string = scraped[2]
    soup.body.append(new_a)
quickeducation()

def funfact(): # Just a fun fact
    new_tags('ff', 'Fun Fact')

    scraped = scraper.ff()
    new_p = soup.new_tag('p')
    new_p.string = scraped
    soup.body.append(new_p)
funfact()

def dopeperson(): # Someone who's just super dope
    new_tags('dp', 'Person of the Day')

    scraped = scraper.dp()
    new_p = soup.new_tag('p')
    new_p.string = scraped
    soup.body.append(new_p)
dopeperson()

def photos(): # Cool photos from NASA
    new_tags('pfst', 'Photos from Spacetime')

    scraped = scraper.pfst()[2]
    new_a = soup.new_tag(f'a href={scraper.pfst()[1]}')
    new_a.string = scraped
    soup.body.append(new_a)
photos()

def onthisday(): # On this day __ years ago something interesting happened
    new_tags('otd', 'On this Day')

    scraped = scraper.otd()
    new_p = soup.new_tag('p')
    new_p.string = scraped
    soup.body.append(new_p)
onthisday()

def news(): # Recap of yesterday's events
    new_tags('news', 'News')
    new_ul = soup.new_tag('ul')
    soup.body.append(new_ul)

    stories = scraper.news()[1]
    for i in range(len(stories) - 1):
        if i % 2 == 0:
            link = stories[i]
            title = stories[i+1]

            new_li = soup.new_tag('li')
            a = soup.new_tag(f'a href={link}')
            a.append(title)
            new_li.append(a)
            new_ul.append(new_li)
news()

# Write final html
html_write = open('email.html', 'w+')
html_write.write(soup.prettify())
html_write.close()