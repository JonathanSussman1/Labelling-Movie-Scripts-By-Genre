from IMSDBScraper import IMSDBScraper
import numpy as np

parser = IMSDBScraper(n_scripts=5, genre = "Adventure")
scripts = parser.get_all_scripts()
print(scripts)