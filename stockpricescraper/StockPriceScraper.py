import bs4
import ezsheets
from Config import (FIRST_ROW, NAME_TO_TICKER, PRICE_FEED_URL, SHEET_NAME,
                    SPREADSHEET_ID)
from selenium import webdriver


def main():
    print("Opening webdriver...")
    driver = webdriver.Chrome()
    allTickerToPrice: list[tuple[str, str]] = []
    for url in PRICE_FEED_URL:
        print("Getting price feed from: " + url)
        tickerToPrice = getPriceFeed(driver, url)
        print(*tickerToPrice, sep="\n")
        allTickerToPrice.extend(tickerToPrice)
    print("Price feed retrieved successfully.")
    driver.quit()

    print("Updating spreadsheet...")
    ss = ezsheets.Spreadsheet(SPREADSHEET_ID)
    sh = ss[SHEET_NAME]
    for index, item in enumerate(allTickerToPrice):
        try:
            ticker = NAME_TO_TICKER[item[0]]
        except KeyError:
            ticker = ""
            print("Ticker not found for: " + item[0])
        sh.updateRow(FIRST_ROW + index, [ticker, item[0], item[1]])
    print("Spreadsheet updated successfully.")


def getPriceFeed(driver: webdriver, url: str) -> list[tuple[str, str]]:
    driver.get(url)
    html = driver.page_source
    priceFeedSoup = bs4.BeautifulSoup(html, "html.parser")
    tableContent = priceFeedSoup.select("td")[4:-2]
    tickerToPrice: list[tuple[str, str]] = []
    for i in range(0, len(tableContent) - 2, 3):
        ticker = tableContent[i].get_text()[3:-1]
        price = tableContent[i + 2].get_text()[2:-3]
        tickerToPrice.append((ticker, price))
    return tickerToPrice


if __name__ == "__main__":
    main()
