import requests, bs4, os, click


URL = "https://imgur.com/search?q="


def image_downloader(search: str) -> None:
    folder_path = os.path.join("output", search)
    os.makedirs(folder_path, exist_ok=True)

    response_object = requests.get(URL + search)
    response_object.raise_for_status()

    soup_object = bs4.BeautifulSoup(response_object.text, "lxml")

    image_elements = soup_object.select("img[alt='']")

    click.echo(click.style("Downloading...", fg="yellow"))

    for i in range(1, len(image_elements)):
        image_element_url = "http:" + image_elements[i].get("src")

        response_object = requests.get(image_element_url)
        response_object.raise_for_status()

        image_file = open(
            os.path.join(folder_path, os.path.basename(image_element_url)), "wb"
        )

        for chunk in response_object.iter_content(100000):
            image_file.write(chunk)
        image_file.close()


@click.command()
@click.option(
    "--search",
    "-s",
    type=str,
    default="Camel",
    help="images to search for and download",
)
def main(search: str) -> None:
    """
    A utility to search and download images from imgur.com
    """
    image_downloader(search)
    click.echo(click.style("Download complete", fg="green"))


main()
