# Task 3: News Headlines Scraper

This Python script scrapes the latest news headlines from [AajTak](https://www.aajtak.in/) and saves them into a text file. It uses `requests` to fetch the webpage and `BeautifulSoup` to parse HTML.

---

## Features

- Scrapes all `<h2>` headlines (top news headlines) from the AajTak homepage.
- Removes duplicates.
- Saves headlines in a text file (`headlines.txt`).
- Optionally saves the file into a subfolder.

---

## Requirements

- Python 3.x
- Libraries:
  - `requests`
  - `beautifulsoup4`

Install required libraries with pip:

```bash
pip install requests beautifulsoup4

📧 Email: prasadtodkar535@gmail.com
