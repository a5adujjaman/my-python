import requests
import dns.resolver
from bs4 import BeautifulSoup
import re

# Function to perform DNS query to find subdomains
def dns_query(domain):
    subdomains = []
    resolver = dns.resolver.Resolver()
    try:
        answers = resolver.resolve(domain, 'A')
        subdomains.append(domain)
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
        pass
    return subdomains

# Function to scrape subdomains from HTML content
def scrape_subdomains(url, domain):
    subdomains = set()
    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')
        links = soup.find_all('a', href=True)
        for link in links:
            href = link['href']
            if domain in href:
                subdomain = re.findall(r'://([^/]+)', href)
                if subdomain:
                    subdomains.add(subdomain[0])
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
    return subdomains

# Function to find new subdomains
def find_subdomains(domain):
    subdomains = set()

    # Initial DNS query for the domain
    subdomains.update(dns_query(domain))

    # Scrape the main website for potential subdomains
    main_url = f"http://{domain}"
    subdomains.update(scrape_subdomains(main_url, domain))

    # Print the found subdomains
    for subdomain in subdomains:
        print(subdomain)

if __name__ == "__main__":
    target_domain = "doctolib.de"  # Replace with your target domain
    find_subdomains(target_domain)
