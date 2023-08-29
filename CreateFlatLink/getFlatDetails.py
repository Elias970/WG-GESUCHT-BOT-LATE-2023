
# This method will read the html content from the provided file and return the first flat link in the file
from bs4 import BeautifulSoup

def get_flat_details(input_filename, output_filename):
    # Load the HTML content from the provided text
    html_content = open(input_filename, 'r')

    # Create a BeautifulSoup object
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find all div elements with the data-id attribute
    div_elements = soup.find_all('div', {'data-id': True})

    # Initialize a variable to store the result
    result = None

    # Loop through the div elements and find the first non-empty data-id and store it in the result variable
    # The first object with data id is the last uploaded flat
    # get the content from the first <a> tag within the div, because there is the link to the flat
    for div in div_elements:
        data_id = div.get('data-id')
        if data_id:
            # Find the first <a> tag within the current div
            a_tag = div.find('a')
            if a_tag:
                result = a_tag.get('href')
                break

    # Write the result to the output file 
    # add the base url to the result to get the url for message sending
    if result:
        with open(output_filename, 'w') as file:
            file.write("https://www.wg-gesucht.de/nachricht-senden"+result)
        return True
    else:
        print("No suitable data found in the provided scraped HTML file.")
        return False
