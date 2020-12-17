from bs4 import BeautifulSoup
import requests
from random import randint
from selenium import webdriver

def wotd():
    page = requests.get('https://www.merriam-webster.com/word-of-the-day/calendar')
    soup = BeautifulSoup(page.text, 'html.parser')

    # Get word and meaning
    current_day = soup.find(class_="quick-def-box")
    word = current_day.find(class_="wod-l-hover")
    meaning = current_day.find(class_="definition-block")
    meaning = current_day.find('p')

    cell = word.text, meaning.text
    return cell

def qe():
    videos = 'https://www.youtube.com/user/scishow/videos'
    driver = webdriver.Firefox()
    driver.get(videos)
    driver.implicitly_wait(100)

    # Find the title and link of the newest video
    title = driver.find_element_by_id("video-title").get_attribute("title")
    link = driver.find_element_by_id("video-title").get_attribute("href")
    cell = f'=HYPERLINK("{link}", "{title}")'
    driver.close()

    return cell, link, title

def ff():
    page = requests.get('https://www.kickassfacts.com/fact-of-the-day/')
    soup = BeautifulSoup(page.text, 'html.parser')

    # Get fun fact
    fun_fact = soup.find(class_="entry-content herald-entry-content")
    facts = fun_fact.find_all('li')

    cell = facts[randint(0, len(facts)-1)].text
    return cell

def dp():
    page = requests.get('https://www.onthisday.com/today/birthdays.php')
    soup = BeautifulSoup(page.text, 'html.parser')

    # Pick random person from the list
    all_people = soup.find_all('div', class_="section section--highlight section--person-of-interest")
    people = []
    for person in all_people:
        people.append(person.find('p'))

    cell = people[randint(0, len(people)-1)].text
    return cell

def pfst():
    page = requests.get('https://apod.nasa.gov/apod/astropix.html')
    soup = BeautifulSoup(page.text, 'html.parser')

    # Get title and link
    title = soup.find('b').text.strip()
    photo_link = soup.find_all('a')
    photo_link = photo_link[1]
    photo = 'https://apod.nasa.gov/apod/' + photo_link['href']

    # Download photo to use as email attachment
    f = open('pfst.jpg', 'wb')
    f.write(requests.get(photo).content)
    f.close()

    cell = f'=HYPERLINK("{photo}", "{title}")'
    return cell, photo, title

def otd():
    page = requests.get('https://www.onthisday.com/today/events.php')
    soup = BeautifulSoup(page.text, 'html.parser')

    # Pick random event from the list
    all_events = soup.find_all('li', class_="event")
    events = []
    for event in all_events:
        events.append(event.text)

    cell = events[randint(0, len(events)-1)]
    return cell

def news():
    page = requests.get('https://www.reuters.com/')
    soup = BeautifulSoup(page.text, 'html.parser')

    # Intialize cell value
    cell = ''

    # Main story - title and link
    main_story = soup.find(class_="right-now-module")
    main_title = main_story.find(class_="story-title").text.strip()
    link = main_story.find('a', href=True)
    main_link = 'https://www.reuters.com/' + link['href']

    #* Format main story   TITLE|LINK|
    cell += f'{main_title}<'
    cell += f'{main_link}<'

    # Smaller stories - title and link
    mini_stories = []
    minis = soup.find(class_="news-headline-list")
    minis = minis.find_all('article', class_="story")

    #* Format mini stories TITLE<LINK< for spreadsheet
    stories = [] #* Format for html_changer.py
    for story in minis:
        story = story.find('a', href=True)
        title = story.text.strip()
        link = 'https://www.reuters.com/' + story['href']
        cell += f'{title}<'
        cell += f'{link}<'
        stories.append(link)
        stories.append(title)

    return cell, stories
news()