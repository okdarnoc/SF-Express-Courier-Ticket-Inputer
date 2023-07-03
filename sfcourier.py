# First, we import the webbrowser module. This is a standard library in Python,
# and it provides a high-level interface to allow displaying Web-based documents to users.
import webbrowser

# This line prompts the user to input their courier order number.
# The input function in Python allows user input.
order_number = input("輸入順豐運單編號 \n Enter the courier order number: ")

# This line constructs the URL for SF Express tracking using the order number provided by the user.
# String concatenation is used to append the order number to the end of the SF Express URL.
url = "https://ucmp-x.sf-express.com/xaccess/scan/order?reserve=SF" + order_number

# Here, we construct a version of the URL that will be displayed in mobile format.
# The "&view=mobile" is appended to the URL using string concatenation.
mobile_url = url + "&view=mobile"

# This line opens the constructed URL in the default web browser.
# The webbrowser module's open function is used to open the URL.
webbrowser.open(mobile_url)
