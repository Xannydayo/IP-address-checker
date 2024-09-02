import socket
import urllib.parse

def get_ip_address(url):
    """
    This function takes a URL as input and attempts to resolve it to its corresponding IP address.
    If the URL is valid and can be resolved, it returns the IP address as a string.
    If the URL is invalid or cannot be resolved, it returns an error message indicating the issue.
    """
    try:
        # Attempt to retrieve the IP address associated with the provided URL
        ip_address = socket.gethostbyname(url)
        return ip_address
    except socket.gaierror:
        # Handle the case where the URL cannot be resolved
        return "Error: Invalid URL or unable to resolve the IP address. Please check the URL and try again."

# Prompt the user for input, specifically asking for a website URL to check its IP address
website_url = str(input('[+] Please enter the website URL to check its IP address: '))

# Parse the input URL to extract the network location (domain) and pass it to the get_ip_address function
parsed_url = urllib.parse.urlparse(website_url)
ip_address = get_ip_address(parsed_url.netloc)

# Display the result to the user, clearly indicating the IP address associated with the provided website URL
print(f'The IP address of the website "{website_url}" is: {ip_address}')
