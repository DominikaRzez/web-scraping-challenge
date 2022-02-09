<h1>Mission to Mars</h1>
<h4>Web Scraping Challenge</h4>
<br>
<p><ul>The following repository contains Missions_to_Mars folder with:
<li>Jupyter Notebook</li>
<li>scrape_mars.py file</li>
<li>app.py file</li>
<li>screenshort folder with image of the final application result</li>
<li>templates folder with index file containing HTML code, using Bootstrap to style the webpage</li>
</ul>
</p>
<br>
<p><strong> The Jupyter Notebook</strong> contains initial scraping code.
  <ul>
    <li>Scrapes the most recent <a href="https://redplanetscience.com/">NASA news</a> and collects the latest articles title and paragraph</li>
    <li>Scrapes the <a href="https://spaceimages-mars.com/">URL</a> for the featured image</li>
    <li>Scrapes the table containing <a href="https://galaxyfacts-mars.com/">Mars facts</a></li>
    <li>Scrapes high resolution images for each of <a href="https://marshemispheres.com/">Mars hemispheres</a> and saves image urls and titles into a dictionary</li>
   </ul>
</p>
<br>
<p><strong>The file scrape_mars.py</strong> contains a function called scrape that executes all of the scraping code and holds scraped data in one Python dictionary
<br>
<strong>The Flask App</strong> connects, fetches and inserts data to and from a MongoDB. The script imports the scrape function, queries Mongo database and passes the mars data into an HTML template to display data.</p>
  
  
<p>The assignment utilises Flask, BeautifulSoup, Splinter, MongoDB, Bootstrap.</p>
