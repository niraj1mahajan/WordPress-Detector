import sys
import requests
from termcolor import colored

# check if a website is using WordPress
def is_wordpress(url):
    try:
        response = requests.get(url)
        if "wp-content" in response.text:
            return True
        else:
            return False
    except:
        return False

# read the input file and check each domain
def check_domains(filename):
    with open(filename, "r") as file:
        for line in file:
            url = line.strip()
            if is_wordpress(url):
                print(colored(url, "green") + " is using WordPress")
            else:
                print(colored(url, "red") + " is not using WordPress")

if __name__ == "__main__":
    print("WordPress Detector Tool")
    if len(sys.argv) != 2:
        print("Usage: python wordpress_detector.py <input_file>")
        sys.exit(1)
    filename = sys.argv[1]
    check_domains(filename)
