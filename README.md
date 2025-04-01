# Stock Price Scraper
Stock Price Scraper is a Python script that scrapes stock prices from public watchlists or portfolios on i3investor to Google Sheet.

## Background
I keep track of my portfolio in a Google Sheet. To fetch stock prices, the straightforward way is to use [GOOGLEFINANCE](https://support.google.com/docs/answer/3093281?hl=en) but unfortunately, it no longer supports most international exchanges. An alternative is to scrape the information through App Script. Whether this works depends on the website's policy which often prevents web scraping.

## How It Works
1. [i3investor](https://klse.i3investor.com/) allows public watchlists or portfolios to be shared as a jsp page.
<figure>
  <img src="screenshots/i3investor_portfolio.png" alt="Example watchlist on i3investor">
  <figcaption style="text-align:center">Example watchlist on i3investor</figcaption>
</figure>

2. It relies on JavaScript to render the content. As such, the HTML returned by `requests.get()` will not include the dynamically generated content. Instead, we use Selenium to render the page.

3. The page displays the portfolio in the form of a `table`. With `BeautifulSoup`, the information is extracted from the `td` tags.

4. Now, what's left is to write the results to the Google Sheet. This is done through the `ezSheets` package.

5. To enable the script to access the Google Sheet, follow the steps [here](https://developers.google.com/workspace/drive/api/quickstart/python) to enable the API and download the credentials to the root directory of this project as `credentials-sheets.json`.

6. 

<figure>
  <img src="screenshots/googlesheet.png" alt="Example Outcome in Google Sheet">
  <figcaption style="text-align:center">Example Outcome in Google Sheet</figcaption>
</figure>

## How to Use the Script
1. Open Config.py, edit:
    1. ID of your Google Sheet
    2. Name of the sheet in the Google Sheet
    3. List of URLs for public watchlists or portfolios on i3investor (eg. "https://klse.i3investor.com/servlets/pfs/123456plg.jsp")

## Running Stock Price Scraper in a Virtual Environment
Python virtual environments are isolated spaces that allow you to manage project-specific dependencies without affecting your system's global Python installation. To do so, follow the steps below.

### Setting up Virtual Environment
1. [Install Python](https://www.python.org/downloads/)
2. Double click on `setup.bat`. Wait for the setup to complete.

```bash
Creating virtual environment...
Activating virtual environment...
Installing required packages...
Collecting attrs==25.3.0 (from -r ./requirements.txt (line 1))
  Using cached attrs-25.3.0-py3-none-any.whl.metadata (10 kB)
Collecting beautifulsoup4==4.13.3 (from -r ./requirements.txt (line 2))
  Using cached beautifulsoup4-4.13.3-py3-none-any.whl.metadata (3.8 kB)
...Trimmed...
Done!
Press any key to continue . . .
```

## Running Stock Price Scraper
1. Double click on `run.bat`. Wait for the script to finish running.
```bash
Activating virtual environment...
Running script...
Opening webdriver...
...Trimmed...
Getting price feed from: https://klse.i3investor.com/servlets/pfs/120437plg.jsp
('VITROX', '3.01')
('MATRIX', '1.36')
('PADINI', '2.15')
('MAYBANK', '10.12')
('SUNREIT', '1.82')
('GENM', '1.66')
```