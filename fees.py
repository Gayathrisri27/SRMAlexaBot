# fees.py
import requests
from bs4 import BeautifulSoup

def fetch_fee_status():
    url = 'https://www.srmist.edu.in/admission-india/fee-structure'
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        fee_status = soup.find('div', class_='fees').text.strip()
        return fee_status
    except requests.RequestException as e:
        print(f"Error fetching fee status: {e}")
        return "Error fetching fee status"
