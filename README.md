# WG-GESUCHT-BOT 2023

The WG-GESUCHT-BOT 2023 is a tool designed for scientific purposes only. Please note that using this bot for any other purposes, including personal or commercial use, may be illegal. Use it responsibly and in compliance with all applicable laws.

## Prerequisites

Before you can use the bot, you need to have the following software and files installed/configured:

1. **Python 3:** Make sure you have Python 3 installed on your system. You can download it from [Python's official website](https://www.python.org/downloads/).

2. **Pip:** Pip is a package manager for Python. If you don't have it installed, follow the installation instructions [here](https://pip.pypa.io/en/stable/installation/).

3. **Playwright:** Playwright is a browser automation tool. Install it using pip with the following command:

```
pip install playwright
```


## Configuration

1. Add your WG-GESUCHT login credentials to `credentials.txt`

```
YourEmailAddress
YourPassword
```


2. Open the WG-GESUCHT website and select whether you are looking for a "WG" (shared apartment) or "Wohnung" (apartment) and enter your desired city.

3. Optionally, you can set up filters to refine your search on the WG-GESUCHT website.

4. Copy the generated search link from the WG-GESUCHT website.

5. Paste the copied search link into a file named `searchlink.txt`.
6. Paste your message in `message_text`without "hi". The Bot will add the name and "Hi" later

## Usage

To run the bot, use the following command:
```python3 main.py```


The bot will then use your provided credentials and search link to perform automated actions on the WG-GESUCHT website. Please ensure you have the necessary permissions to use this bot for research purposes.

## Disclaimer

This bot is intended solely for scientific research purposes and should be used responsibly and in accordance with all applicable laws and terms of service of the WG-GESUCHT website. Unauthorized or inappropriate use of this bot may have legal consequences.

**Note:** The use of this bot may violate the terms of service of WG-GESUCHT. Be sure to review and comply with their policies before using this tool.
