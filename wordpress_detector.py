import sys
import requests
from termcolor import colored

def check_domains(filename):
    try:
        with open(filename, "r") as file:
            domains = file.read().splitlines()
    except FileNotFoundError:
        print(colored("Error: File not found", "red"))
        return

    wordpress_domains = []
    non_wordpress_domains = []

    for domain in domains:
        try:
            response = requests.get(f"http://{domain}")
        except (requests.exceptions.Timeout, requests.exceptions.ConnectionError):
            print(colored(f"Error: Unable to connect to {domain}", "red"))
            continue

        if "wp-content" in response.text:
            wordpress_domains.append(domain)
            print(colored(f"{domain} is using WordPress", "green"))
        else:
            non_wordpress_domains.append(domain)
            print(colored(f"{domain} is not using WordPress", "red"))

    with open("wordpress_domains.txt", "w") as file:
        file.write("\n".join(wordpress_domains))

    print(colored(f"Total domains checked: {len(domains)}", "blue"))
    print(colored(f"WordPress sites found: {len(wordpress_domains)}", "green"))
    print(colored(f"Non-WordPress sites found: {len(non_wordpress_domains)}", "red"))

if __name__ == "__main__":
    print(colored("WordPress Detector Tool", "yellow"))

    if len(sys.argv) < 2:
        print(colored("Error: Please specify an input file", "red"))
        print(colored("Usage: python wordpress_detector.py <filename>", "yellow"))
    else:
        filename = sys.argv[1]
        check_domains(filename)
