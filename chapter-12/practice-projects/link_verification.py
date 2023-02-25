import requests, bs4


response_object = requests.get("https://www.thetechbasket.com/most-useful-websites/")
response_object.raise_for_status()

soup_object = bs4.BeautifulSoup(response_object.text, "lxml")
link_elements = soup_object.select("a[rel='noopener']")

for link_element in link_elements:
    link_element_url = link_element.get("href")

    try:
        response_object = requests.get(link_element_url)
    except requests.exceptions.SSLError as bad_url:
        print(f"[bad_url]: {bad_url}")
    except Exception as e:
        print(f"[error]: {e}")

    if response_object.status_code == requests.codes.not_found:
        print("Broken link -- " + link_element_url)
    else:
        print(link_element_url)
