from bs4 import BeautifulSoup
from requests import get
from typing import Generator, Tuple

class UCIScraper:
    def __init__(self, *,  verbose: bool = False):
        self.base_url = "https://archive.ics.uci.edu/ml/"
        self.links_location = "datasets.php"
        self.verbose = verbose
        self.headers = ("Name", "Data Set Characteristics", "Attribute Characteristics", "Associated Tasks", "Number of Instances",
                        "Number of Attributes", "Missing Values", "Area", "Date Donated", "Number of Web Hits")

    def log(self, *values: object) -> None:
        if self.verbose:
            print(*values)

    def links_generator(self, url: str) -> Generator[Tuple[str, str], None, None]:
        self.log("Downloading link from '{}'...".format(url))
        soup = BeautifulSoup(get(url).text, features="lxml")
        self.log("Links downloaded")
        tab = soup.body.find_all("table")[1].find_all("table", recursive=True)[3]
        for tr in tab.find_all("tr", recursive=False)[1:]:
            a = tr.td.find_all("a", recursive=True, href=True)[1]
            link = a["href"]
            name = a.contents[0]
            yield (name, self.base_url + link)

    def generate_links_file(self, filename: str) -> None:
        self.log("Generating links file")
        with open(filename, "w", encoding="utf-8") as links_file:
            print("Name", "Link", sep="\t", file=links_file)
            for (name, link) in self.links_generator(self.base_url + self.links_location):
                print(name, link, sep="\t", file=links_file)
        self.log("Links file generated, saved as '{}'".format(filename))

    def datasets_generator(self, links_filename: str) -> Generator[Tuple[str,...], None, None]:
        with open(links_filename, "r", encoding="utf-8") as links_file:
            links = [link.strip().split("\t")
                     for link in links_file.readlines()[1:]]
            link_count = len(links)
            for index, (name, link) in enumerate(links):
                self.log("Getting dataset {} out of {}...".format(
                    index+1, link_count))
                soup = BeautifulSoup(get(link).text, features="lxml")
                try:
                    tab = soup.body.find_all("table")[3]
                    db_data = [
                        name, # Name
                        tab.find_all("tr")[0].find_all("td")[1].p.contents[0].strip("\""), # Data Set Characteristics
                        tab.find_all("tr")[1].find_all("td")[1].p.contents[0].strip("\""), # Attribute Characteristics
                        tab.find_all("tr")[2].find_all("td")[1].p.contents[0].strip("\""), # Associated Tasks
                        tab.find_all("tr")[0].find_all("td")[3].p.contents[0].strip("\""), # Number of Instances
                        tab.find_all("tr")[1].find_all("td")[3].p.contents[0].strip("\""), # Number of Attributes
                        tab.find_all("tr")[2].find_all("td")[3].p.contents[0].strip("\""), # Missing Values
                        tab.find_all("tr")[0].find_all("td")[5].p.contents[0].strip("\""), # Area
                        tab.find_all("tr")[1].find_all("td")[5].p.contents[0].strip("\""), # Date Donated
                        tab.find_all("tr")[2].find_all("td")[5].p.contents[0].strip("\"")  # Number of Web Hits
                    ]
                    for i in range(len(db_data)):
                        if db_data[i].lower() == "N/A":
                            db_data[i] = ""
                    self.log("Loaded")
                    yield tuple(db_data)
                except Exception as e:
                    self.log("Exception in database {} - {}".format(link, e))

    def generate_datasets_file(self, links_filename: str, filename: str) -> None:
        self.log("Generating datasets file")
        with open(filename, "w", encoding="utf-8") as links_file:
            print(*self.headers, sep="\t", file=links_file)
            for dataset in self.datasets_generator(links_filename):
                print(*dataset, sep="\t", file=links_file)
        self.log("Datasets file generated, saved as '{}'".format(filename))

if __name__ == "__main__":
    scraper = UCIScraper(verbose=True)
    scraper.generate_links_file("links.tsv")
    scraper.generate_datasets_file("fixed_links.tsv", "datasets.tsv")
