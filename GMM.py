from IMSDBScraper import IMSDBScraper
import numpy as np

parser = IMSDBScraper(n_scripts=1,genre='all')
scripts = parser.get_all_scripts()
print(scripts)