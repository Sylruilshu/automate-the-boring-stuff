import requests, bs4, os, json, datetime, threading


with open("metadata_test.json", "r") as json_file:
    website_metadata = json.load(json_file)


def download_latest_comic(website_info: dict) -> None:
    response = requests.get(website_info["url"], headers=website_info["header"])
    response.raise_for_status()

    soup = bs4.BeautifulSoup(response.text, "lxml")
    image_elements = soup.select(website_info["image selector"])
    date_elements = soup.select(website_info["date selector"])

    date = date_elements[website_info["date element number"]].text

    try:
        new_date = datetime.datetime.strptime(date, "%B %d, %Y")
        old_date = datetime.datetime.strptime(website_info["date"], "%B %d, %Y")
    except ValueError:
        new_date, old_date = reformat_date(date, website_info)

    if new_date > old_date:
        website_info["date"] = date

        with open("metadata_test.json", "w") as json_file:
            json.dump(website_metadata, json_file)

        comic_url = image_elements[website_info["image element number"]].get("src")
        print(
            "Downloading:",
            os.path.basename(comic_url),
            "--- From:",
            website_info["url"],
        )

        response = requests.get(comic_url, headers=website_info["header"])
        response.raise_for_status()

        os.makedirs("test", exist_ok=True)

        with open(
            os.path.join("test", os.path.basename(comic_url)), "wb"
        ) as image_file:
            for chunk in response.iter_content(100000):
                image_file.write(chunk)
    else:
        print(
            f"Comic from {website_info['url']} is up to date --- ({website_info['date']})"
        )


def reformat_date(date: str, website_info: dict):
    date = date.strip()
    date = date.split(" ")
    reconstructed_new_date = f"{date[1]} {date[2][:-3]}, {date[3]}"

    if datetime.datetime.strptime(website_info["date"], "%B %d, %Y"):
        old_date = datetime.datetime.strptime(website_info["date"], "%B %d, %Y")
    else:
        test = website_info["date"].split(" ")
        reconstructed_old_date = f"{test[1]} {test[2][:-3]}, {test[3]}"
        old_date = datetime.datetime.strptime(reconstructed_old_date, "%B %d, %Y")

    new_date = datetime.datetime.strptime(reconstructed_new_date, "%B %d, %Y")
    # old_date = datetime.datetime.strptime(reconstructed_old_date, "%B %d, %Y")

    return new_date, old_date


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
