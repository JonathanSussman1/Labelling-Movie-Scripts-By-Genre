from IMSDBScraper import IMSDBScraper
from preprocessing import PreprocessingObj

import numpy as np

parser = IMSDBScraper(n_scripts=5, genre = "Adventure")
scripts = parser.get_all_scripts()
print(scripts[0][0])

preprocessor = PreprocessingObj(n_scripts_to_add=40, n_scripts_to_randomly_remove=20, n_genre_scripts_to_add=11, n_genre_scripts_to_randomly_remove=1)
print(preprocessor.allscripts)
print(preprocessor.genrescripts["Mystery"])