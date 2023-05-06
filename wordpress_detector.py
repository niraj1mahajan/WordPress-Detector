import sys
import concurrent.futures
import requests

wordpress_strings = ['wp-content', 'wp-admin', 'wp-includes']

if len(sys.argv) != 2:
    print('\033[91mUsage: python wordpress_detector.py <filename>\033[0m')
    sys.exit(1)

filename = sys.argv[1]

with open(filename, 'r') as f:
    domains = f.read().split()

def process_domain(domain):
    try:
        response = requests.head('http://' + domain, timeout=5)
        if any(string in response.content.decode().lower() for string in wordpress_strings):
            return domain
        else:
            return None
    except Exception as e:
        return None

with concurrent.futures.ThreadPoolExecutor() as executor:
    results = list(executor.map(process_domain, domains))

wordpress_domains = [domain for domain in results if domain is not None]

with open('wordpress_domains.txt', 'w') as f:
    for domain in wordpress_domains:
        f.write(domain + '\n')

print('\n\033[92mWordPress sites:', *wordpress_domains, sep='\n', end='\033[0m\n')
