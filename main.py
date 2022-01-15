from bs4 import BeautifulSoup
import requests
import time
import os
import io

pages_urls=[]

SITE='https://lightnovels.me'

def scrape_chapter(chapter_link):
    try:
        html_text=requests.get(chapter_link).text
    except:
        print('no internet connection')
    soup=BeautifulSoup(html_text,'lxml')
    title=soup.find('h1',class_='text-lg m-0 dark:text-text-dark-mode-light').text
    content=soup.find('div',class_='text-xl text-justify dark:text-text-dark-mode-light dark:border-gray-300').text
    return title,content

def scrape():
    novel=input('Enter the link: ')
    try:
        html_text=requests.get(novel).text
    except:
        print('no internet connection')
    soup=BeautifulSoup(html_text,'lxml')
    
    global novel_title
    novel_title=soup.find('h1',class_='text-2xl font-bold m-2.5 uppercase text-center border-2 border-t-0 border-l-0 border-r-0 border-gray-200 border-solid dark:border-gray-400 dark:text-text-dark-mode-light').text
    
    soup=BeautifulSoup(html_text,'lxml')
    chapters=soup.find_all('li',class_='w-full my-1 dark:text-text-dark-common dark:hover:text-text-dark-common-hover')
    scraping(chapters)

def scraping(chapters):
    global path
    global index
    parent_dir=os.getcwd()
    directory=novel_title
    path = os.path.join(parent_dir, directory)
    try:
        os.mkdir(path)
        print(f"Directory {directory} created")
    except: 
        print(f'Directory {directory} already exist')
    for index,chapter in enumerate(chapters):
        print(f'saving chapter {index+1}')
        if os.path.exists(f'{path}/{index+1}.txt'):
            print('already exists > skipping......')
            continue
        with io.open(f'{path}/{index+1}.txt','w',encoding='utf-8') as f:
            link=chapter.a['href']
            title,content=scrape_chapter(SITE+link)
            f.write('~'*10)
            f.write(title)
            f.write('~'*10)
            f.write(content)
            f.write('~'*10)
            f.write('~'*10)
        print(f'chapter saved {index+1}')



if __name__ == '__main__':
    while True:
        try:
            scrape()
        except:
            print('an error accured')
        time_wait=1
        print(f'waiting {time_wait} days')
        time.sleep(time_wait*86400)


