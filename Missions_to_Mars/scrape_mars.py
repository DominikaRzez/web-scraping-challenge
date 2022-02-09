# Dependencies
from splinter import Browser
from bs4 import BeautifulSoup as bs
import pandas as pd
import time
from webdriver_manager.chrome import ChromeDriverManager

def scrape_info():
    # Set up Splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    
    # Define url address, visit the Mars News Site
    url = 'https://redplanetscience.com/'
    browser.visit(url)

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")

    # Saving only first element to collect the latest data
    title_art = soup.find_all('div', class_='content_title')[0].text
    para = soup.find_all('div', class_='article_teaser_body')[0].text

    # Define url address, visit JPL Mars Space Images
    url = 'https://spaceimages-mars.com/'
    browser.visit(url)

    # Find image source
    html = browser.html
    soup = bs(html, 'html.parser')

    img_src = soup.find_all('img')[1]["src"]
    # Combine base url with image source to get images url
    featured_image_url = url + img_src

    # Define url, visit Mars Facts webpage
    url = 'https://galaxyfacts-mars.com/'

    # Use Pandas to scrape through the table
    table = pd.read_html(url)
    # Cleaning the table
    df = table[0]
    df2 = df.set_index(keys=0)
    df2.index.name=None
    df2.columns = [''] * len(df2.columns)
    # Generating html table from DataFrame
    html_table = df2.to_html(header=False)
    # Striping unwanted newlines to clean up the table
    html_table = html_table.replace('\n', '')
    # Saving html to a file
    df2.to_html('table.html')

    # Define url address, visit the astrogeology site
    url = 'https://marshemispheres.com/'
    browser.visit(url)

    # Creating empty list to hold dictionaries with img title and url
    hemisphere_image_urls = []
    # Creating a loop to collect all of the desired data
    for x in range (0,4):
        time.sleep(1)
        # HTML object
        html = browser.html
        # Parse HTML with Beautiful Soup
        soup = bs(html, 'html.parser')
        # Find linked title and go through to the each hemisphere page
        href = soup.find_all('h3')[x].text
        browser.links.find_by_partial_text(href).click()
        # HTML object
        html = browser.html
        # Parse HTML with Beautiful Soup
        soup = bs(html, 'html.parser')
        # Scrape hemisphere page for img url and title
        img_url = soup.find_all('img', class_='wide-image')[0]['src']
        full_url = url + img_url
        title = soup.find_all('h2', class_='title')[0].text
        # Create dictionary and append 
        dictionaries = {"title": title, "img_url": full_url}
        hemisphere_image_urls.append(dictionaries)
        # Click back to the main page
        back = soup.find_all('h3')[1].text
        browser.links.find_by_partial_text(back).click()

    # Creating dictionary to hold all of the scraped data
    mars_data = {
        "title_art": title_art,
        "para": para,
        "featured_image_url": featured_image_url,
        "html_table": html_table,
        "hemisphere_image_urls": hemisphere_image_urls
        }

    # Close the browser after scraping
    browser.quit()

    # Return results
    return mars_data