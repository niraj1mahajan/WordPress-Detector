# WordPress Detector

WordPress Detector is a Python script that checks whether a list of domains are running WordPress or not. It does this by sending a HEAD request to the root URL of each domain, and checking for the presence of certain strings in the response body that indicate that the website is running WordPress.

## Usage

To use WordPress Detector, you need to have Python 3 installed on your system. You can download Python 3 from the official website: https://www.python.org/downloads/

1. Clone or download the WordPress Detector repository from GitHub.
2. Open a terminal or command prompt and navigate to the directory where the script is located.
3. Run the script with the following command:

python wordpress_detector.py <filename>


Replace `<filename>` with the name of the file that contains the list of domains you want to check. Each domain should be on a separate line in the file.

For example, if your file is called `mydomains.txt`, you would run the script with the following command:

python wordpress_detector.py mydomains.txt


4. The script will output the list of domains that are running WordPress to the console, and also write them to a file called `wordpress_domains.txt` in the same directory as the script.

WordPress sites will be printed in green color and non-wordpress sites will be printed in red color.

## Optimizations

The script uses concurrent.futures module to run the `process_domain` function on multiple domains concurrently using a thread pool. The `head` method of the `requests` library is used instead of `get`, and a `timeout` of 5 seconds is set to avoid waiting too long for unresponsive websites.

## License

WordPress Detector is licensed under the MIT License. See the `LICENSE` file for more details.
