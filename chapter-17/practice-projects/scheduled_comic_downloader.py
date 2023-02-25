import requests, bs4, os, pickle, datetime, threading


with open("website_metadata.pkl", "rb") as pickle_file:
    website_metadata = pickle.load(pickle_file)


def download_latest_comic(website_info: dict) -> None:
    response = requests.get(website_info["url"], headers=website_info["header"])
    response.raise_for_status()

    soup = bs4.BeautifulSoup(response.text, "lxml")
    image_elements = soup.select(website_info["image selector"])
    date_elements = soup.select(website_info["date selector"])

    date = date_elements[website_info["date element number"]].text

    old_date = datetime.datetime.strptime(website_info["date"], "%B %d, %Y")
    new_date = datetime.datetime.strptime(date, "%B %d, %Y")

    if new_date > old_date:
        website_info["date"] = date

        with open("website_metadata.pkl", "wb") as pickle_file:
            pickle.dump(website_metadata, pickle_file)

        comic_url = image_elements[website_info["image element number"]].get("src")
        print(
            "Downloading:",
            os.path.basename(comic_url),
            "--- From:",
            website_info["url"],
        )

        response = requests.get(comic_url, headers=website_info["header"])
        response.raise_for_status()

        os.makedirs("comics", exist_ok=True)

        with open(
            os.path.join("comics", os.path.basename(comic_url)), "wb"
        ) as image_file:
            for chunk in response.iter_content(100000):
                image_file.write(chunk)
    else:
        print(
            f"Comic from {website_info['url']} is up to date --- ({website_info['date']})"
        )


download_threads = []
for i in range(len(website_metadata)):
    website_info = website_metadata[i]
    download_thread = threading.Thread(
        target=download_latest_comic, args=(website_info,)
    )
    download_threads.append(download_thread)
    download_thread.start()

for download_thread in download_threads:
    download_thread.join()

print("Done.")
