from IMSDBScraper import IMSDBScraper
import numpy as np

parser = IMSDBScraper(n_scripts=100)
scripts = parser.get_all_scripts()
print(scripts[0])