import time
import requests
import sys
import chromedriver_autoinstaller
from selenium import webdriver

chromedriver_autoinstaller.install()

def check_redirection(url):
    # Create a new instance of the Chrome driver
    driver = webdriver.Chrome()

    while True:
        # Open the URL
        driver.get(url)

        # Get the current URL after any redirection
        current_url = driver.current_url

        # Check if the current URL is the same as the original URL
        if current_url == url:
            output = "Book Now"
        else:
            output = "Not Yet"

        # Print the output
        print(output)
        
        # Check if there's no redirection
        if output == "Book Now":
            # Define your Discord webhook URL
            webhook_url = ""

            # Create a payload with the output as the content
            payload = {
                "content": output
            }

            # Send the payload to the Discord webhook
            response = requests.post(webhook_url, json=payload)

            # Check if the request was successful
            if response.status_code != 204:
                print("Failed to send output to Discord webhook.")

            # Exit the loop and terminate the script
            break

        # Wait for 30 minutes before checking again
        time.sleep(3600)

    # Close the browser window
    driver.quit()

# Check if the URL argument is provided
if len(sys.argv) < 2:
    print("Please provide a URL.")
else:
    # Extract the URL from the command-line argument
    url = sys.argv[1]

    # Call the function to continuously check redirection
    check_redirection(url)
