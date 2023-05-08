import requests
import sys


def check_domains(filename):
    wordpress_domains = []
    with open(filename, "r") as file:
        domains = file.read().splitlines()
        total_domains = len(domains)
        for i, domain in enumerate(domains):
            try:
                response = requests.get(f"http://{domain}")
                if "wp-content" in response.text:
                    wordpress_domains.append(domain)
                    print(f"\033[92m{i+1}/{total_domains}: {domain} is using WordPress\033[0m")
                else:
                    print(f"\033[91m{i+1}/{total_domains}: {domain} is not using WordPress\033[0m")
            except requests.exceptions.RequestException:
                print(f"\033[91m{i+1}/{total_domains}: Unable to connect to {domain}\033[0m")
    with open("wordpress_domains.txt", "w") as file:
        file.write("\n".join(wordpress_domains))


if __name__ == "__main__":
    print("WordPress Detector Tool")
    if len(sys.argv) < 2:
        print("Usage: python wordpress_detector.py [filename]")
        sys.exit(1)
    filename = sys.argv[1]
    check_domains(filename)
