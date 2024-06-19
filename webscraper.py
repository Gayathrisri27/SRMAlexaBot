import requests
from bs4 import BeautifulSoup

def search_fee_status(query=None):
    urls = [
        "https://sp.srmist.edu.in/srmiststudentportal/students/loginManager/youLogin.jsp",
        "https://www.youtube.com/@SRMeducation",
        "https://www.srmist.edu.in/","https://www.srmhospital.co.in/","https://www.srmist.edu.in/contact-us/","https://www.google.com/maps/dir/12.9359996,80.1406682/R2FV%2B6Q7+SRM+Institute+of+Science+and+Technology,+Potheri,+SRM+Nagar,+Kattankulathur,+Tamil+Nadu+603203/@12.8805489,80.0086329,12z/data=!3m1!4b1!4m9!4m8!1m1!4e1!1m5!1m1!1s0x3a52f712b82a78d9:0xfdb944a3aee53831!2m2!1d80.044416!2d12.823033?entry=ttu"
    ]

    for url in urls:
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            # You can parse the HTML content here to extract the fee status
            # For example:
            if url == "https://sp.srmist.edu.in/srmiststudentportal/students/loginManager/youLogin.jsp":
                fee_status_element = soup.find('div', class_='fee-status')
                if fee_status_element:
                    return fee_status_element.text.strip()
                else:
                    return "No fee status found."
            else:
                return f"URL: {url} does not contain fee status information."
        except requests.RequestException as e:
            print(f"Error searching: {e}")
            return "Error searching"