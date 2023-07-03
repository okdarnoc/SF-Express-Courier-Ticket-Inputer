# SF-Express-Courier-Ticket-Inputer
This simple python script allows you to input your SF Express Courier Ticket Number instead of manually editing the url.

## Description

The script simplifies the process of tracking your SF Express courier by prompting you to input your ticket number directly into the terminal. Once the ticket number is provided, the script generates the corresponding tracking URL and opens it in your default web browser.

## Use Case

This script is useful when you need to quickly check the status of your SF Express courier. Instead of navigating to the SF Express website and manually entering your ticket number, this script automates these steps, making the tracking process more efficient. Simply run the script, input your ticket number when prompted, and get your courier status.

## Getting Started

### Prerequisites

The only requirement to run this script is Python. The script utilizes the `webbrowser` module, which comes standard with Python, thus no additional installations are needed.

### Usage

1. Save the script in a file, for example `sfexpress.py`.
2. Run the script from your terminal with `python sfexpress.py`.
3. When prompted, input your SF Express courier ticket number.

## Code

Here's the complete script:

```python
import webbrowser

order_number = input("Enter the courier order number: ")
url = "https://ucmp-x.sf-express.com/xaccess/scan/order?reserve=SF" + order_number
mobile_url = url + "&view=mobile"
webbrowser.open(mobile_url)
```

## License
This project is licensed under the MIT License.
Please note that this script is for convenience and doesn't replace any official SF Express tracking tools. Always refer to the official SF Express website or customer service for accurate information.

