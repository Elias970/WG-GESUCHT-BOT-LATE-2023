import time
import random
from CreateFlatLink.getFlatDetails import get_flat_details
from CreateFlatLink.scrapeFromPage import make_request_and_save_to_file
from Browserautomate.send_message_playwright import send_message_with_playwright


def main():
    #endless loop
    while True:
        # wait for 10 seconds
        print("restart")
        time.sleep(random.randint(123, 158))
            # File to save the scraped HTML to
        input_filename = 'bot_internal/scraped.txt'
        output_filename = 'bot_internal/newestFlatLinkDetails.txt'
        cache_filename = 'bot_internal/cache.txt'
        playwrightURL = None
        email =None
        password =None
        # read the credentials from file
        with open("credentials.txt", "r") as file:
            email = file.readline().strip()
            password = file.readline().strip()
        # read the search link from file
        link_path="./searchLink.txt"
        with open(link_path, "r") as file:
                searchLink = file.read().strip()
        # read the last newest flat link from file and save it in a variable to compare it later
        with open(output_filename, 'r') as lastNewestFlatLink:
            lastNewestFlatLink = lastNewestFlatLink.read()
        # read the cache file to get messaged flats 
        with open(cache_filename, 'r') as cache:
            flatCache = cache.read()

        # Headers to pretend to be a browser
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

        # 1. Make a request to the URL
        response = make_request_and_save_to_file(searchLink, headers,input_filename)
        print(response)
        #2 extract the newest flat link from the html file and save it to a file
        if get_flat_details(input_filename, output_filename):
            print("Flat details written to file.")
        else:
            print("writing details to file failed.")

        #3 Compare the last flat link with the newest flat link 
        # compare old with new link, if new message, just apply the message
        # first time the bot is run, there is no old link, so just send the message
        with open('bot_internal/newestFlatLinkDetails.txt', 'r') as newestFlatLink:
            newestFlatLink = newestFlatLink.read()
            playwrightURL = newestFlatLink
        if lastNewestFlatLink != newestFlatLink and newestFlatLink not in flatCache:
            print ("***** WOW, NEW FLAT FOUND *****")
            send_message_with_playwright(playwrightURL, email, password)
            with open(cache_filename, 'a') as file:
                file.write(playwrightURL + ";\n")
        else:
            print("No new flat found.")    


if __name__ == "__main__":
    main()
