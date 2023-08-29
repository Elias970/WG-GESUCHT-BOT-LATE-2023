from playwright.sync_api import sync_playwright

from Browserautomate.create_message import create_message
def send_message_with_playwright(newestflatLink, email, password):


    with sync_playwright() as p:
        print ("+++++++++++++"+email, password)
        browser = p.chromium.launch()  # Starte den Browser im "headful"-Modus
        page = browser.new_page()
        page.goto(newestflatLink)
        # wait for cookie banner to appear
        page.wait_for_selector('text="Settings"')
        # decline cookies
        page.click('text="Settings"')
        page.click('text="Save"')
        #click on the login button on page after declining cookies
        page.click('text="Bitte loggen Sie sich hier ein."')
        # fill in email and password
        page.fill('input[name="login_email_username"]',email)
        page.fill('input[name="login_password"]',password)
        page.click('#login_submit')
        page.click('#sicherheit_bestaetigung')
        # get Name of uploader
        element = page.wait_for_selector('.col-xs-10.col-sm-12')
        uploaderLine = element.inner_text()
        # fill in message in message_input with input from text file

        page.click('#message_input')
        page.fill('#message_input',create_message(uploaderLine) )
        #wait for 5 seconds to see what's happening
        #page.wait_for_timeout(50000)
        # send message
        page.click('text="Nachricht senden"')
        browser.close()
        print ("MESSAGE SENT TO " + uploaderLine)