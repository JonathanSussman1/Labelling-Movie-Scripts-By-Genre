from IMSDBScraper import IMSDBScraper
from random import sample

# IMSDBScraper.py gets a fixed, in-order list of scripts of form [(speaker, line), (speaker2, line2), ... (speaker_N, line_N)] 
# from the IMSDB web database. This class uses IMSDBScraper.py to retreive a random base of scripts 
# from all genres (self.allscripts), as well as a dictionary of a number of random scripts that represent each 
# genre (self.genrescripts). 
# No scripts overlap between self.allscripts and self.genrescripts, although there may be overlapping scripts
# between genres in self.genrescripts (for example, genrescripts["Action"] and genrescripts["Adventure"] may contain 
# one or more of the same script). 
# This class serves as a way to break up the database of scripts into a corpus.

class PreprocessingObj:
  # Args:
  #     n_scripts_to_add: number of scripts to be added to self.allscripts IN TOTAL
  #     n_scripts_to_randomly_remove: This can be thought of as a seed, but if n_scripts_to_add 
  #                                   + n_scripts_to_randomly_remove > the number of scripts available from IMSDB,
  #                                   the program will not work.
  #     n_genre_scripts_to_add: number of total scripts to be added to self.genrescripts PER EACH GENRE
  #
   def __init__(self, n_scripts_to_add, n_scripts_to_randomly_remove, n_genre_scripts_to_add, n_genre_scripts_to_randomly_remove):
      self.scripts = (self.load_scripts_corpus(n_scripts_to_add, n_scripts_to_randomly_remove, n_genre_scripts_to_add, n_genre_scripts_to_randomly_remove))
      self.allscripts = self.scripts[0]
      self.genrescripts = self.scripts[1]

   def load_scripts_corpus(self, n_scripts_to_add, n_scripts_to_randomly_remove, n_genre_scripts_to_add, n_genre_scripts_to_randomly_remove):
      parser = IMSDBScraper(n_scripts=n_scripts_to_add + n_scripts_to_randomly_remove,genre='all')
      allscripts = parser.get_all_scripts()
      toRemove = sample(allscripts, n_scripts_to_randomly_remove)
      allscripts = [e for e in allscripts if e not in toRemove]

      parser = IMSDBScraper(n_scripts=n_genre_scripts_to_add+n_genre_scripts_to_randomly_remove,genre='Action')
      Actionscripts = parser.get_all_scripts()
      while not(set([item[0] for item in allscripts]).isdisjoint(set([item[0] for item in Actionscripts]))):
         toRemove = sample(Actionscripts, n_genre_scripts_to_randomly_remove)
         Actionscripts = [e for e in Actionscripts if e not in toRemove]

      parser = IMSDBScraper(n_scripts=n_genre_scripts_to_add+n_genre_scripts_to_randomly_remove,genre='Comedy')
      Comedyscripts = parser.get_all_scripts()
      while not(set([item[0] for item in allscripts]).isdisjoint(set([item[0] for item in Comedyscripts]))):
         toRemove = sample(Comedyscripts, n_genre_scripts_to_randomly_remove)
         Comedyscripts = [e for e in Comedyscripts if e not in toRemove]

      parser = IMSDBScraper(n_scripts=n_genre_scripts_to_add+n_genre_scripts_to_randomly_remove,genre='Family')
      Familyscripts = parser.get_all_scripts()
      while not(set([item[0] for item in allscripts]).isdisjoint(set([item[0] for item in Familyscripts]))):
         toRemove = sample(Familyscripts, n_genre_scripts_to_randomly_remove)
         Familyscripts = [e for e in Familyscripts if e not in toRemove]

      parser = IMSDBScraper(n_scripts=n_genre_scripts_to_add+n_genre_scripts_to_randomly_remove,genre='Horror')
      Horrorscripts = parser.get_all_scripts()
      while not(set([item[0] for item in allscripts]).isdisjoint(set([item[0] for item in Horrorscripts]))):
         toRemove = sample(Horrorscripts, n_genre_scripts_to_randomly_remove)
         Horrorscripts = [e for e in Horrorscripts if e not in toRemove]

      parser = IMSDBScraper(n_scripts=n_genre_scripts_to_add+n_genre_scripts_to_randomly_remove,genre='Romance')
      Romancescripts = parser.get_all_scripts()
      while not(set([item[0] for item in allscripts]).isdisjoint(set([item[0] for item in Romancescripts]))):
         toRemove = sample(Romancescripts, n_genre_scripts_to_randomly_remove)
         Romancescripts = [e for e in Romancescripts if e not in toRemove]

      parser = IMSDBScraper(n_scripts=n_genre_scripts_to_add+n_genre_scripts_to_randomly_remove,genre='Thriller')
      Thrillerscripts = parser.get_all_scripts()
      while not(set([item[0] for item in allscripts]).isdisjoint(set([item[0] for item in Thrillerscripts]))):
         toRemove = sample(Thrillerscripts, n_genre_scripts_to_randomly_remove)
         Thrillerscripts = [e for e in Thrillerscripts if e not in toRemove]

      parser = IMSDBScraper(n_scripts=n_genre_scripts_to_add+n_genre_scripts_to_randomly_remove,genre='Adventure')
      Adventurescripts = parser.get_all_scripts()
      while not(set([item[0] for item in allscripts]).isdisjoint(set([item[0] for item in Adventurescripts]))):
         toRemove = sample(Adventurescripts, n_genre_scripts_to_randomly_remove)
         Adventurescripts = [e for e in Adventurescripts if e not in toRemove]

      parser = IMSDBScraper(n_scripts=n_genre_scripts_to_add+n_genre_scripts_to_randomly_remove,genre='Crime')
      Crimescripts = parser.get_all_scripts()
      while not(set([item[0] for item in allscripts]).isdisjoint(set([item[0] for item in Crimescripts]))):
         toRemove = sample(Crimescripts, n_genre_scripts_to_randomly_remove)
         Crimescripts = [e for e in Crimescripts if e not in toRemove]

      parser = IMSDBScraper(n_scripts=n_genre_scripts_to_add+n_genre_scripts_to_randomly_remove,genre='Fantasy')
      Fantasyscripts = parser.get_all_scripts()
      while not(set([item[0] for item in allscripts]).isdisjoint(set([item[0] for item in Fantasyscripts]))):
         toRemove = sample(Fantasyscripts, n_genre_scripts_to_randomly_remove)
         Fantasyscripts = [e for e in Fantasyscripts if e not in toRemove]

      parser = IMSDBScraper(n_scripts=n_genre_scripts_to_add+n_genre_scripts_to_randomly_remove,genre='Musical')
      Musicalscripts = parser.get_all_scripts()
      while not(set([item[0] for item in allscripts]).isdisjoint(set([item[0] for item in Musicalscripts]))):
         toRemove = sample(Musicalscripts, n_genre_scripts_to_randomly_remove)
         Musicalscripts = [e for e in Musicalscripts if e not in toRemove]

      parser = IMSDBScraper(n_scripts=n_genre_scripts_to_add+n_genre_scripts_to_randomly_remove,genre='Sci-Fi')
      Scifiscripts = parser.get_all_scripts()
      while not(set([item[0] for item in allscripts]).isdisjoint(set([item[0] for item in Scifiscripts]))):
         toRemove = sample(Scifiscripts, n_genre_scripts_to_randomly_remove)
         Scifiscripts = [e for e in Scifiscripts if e not in toRemove]

      parser = IMSDBScraper(n_scripts=n_genre_scripts_to_add+n_genre_scripts_to_randomly_remove,genre='War')
      Warscripts = parser.get_all_scripts()
      while not(set([item[0] for item in allscripts]).isdisjoint(set([item[0] for item in Warscripts]))):
         toRemove = sample(Warscripts, n_genre_scripts_to_randomly_remove)
         Warscripts = [e for e in Warscripts if e not in toRemove]

      parser = IMSDBScraper(n_scripts=n_genre_scripts_to_add+n_genre_scripts_to_randomly_remove,genre='Animation')
      Animationscripts = parser.get_all_scripts()
      while not(set([item[0] for item in allscripts]).isdisjoint(set([item[0] for item in Animationscripts]))):
         toRemove = sample(Animationscripts, n_genre_scripts_to_randomly_remove)
         Animationscripts = [e for e in Animationscripts if e not in toRemove]

      parser = IMSDBScraper(n_scripts=n_genre_scripts_to_add+n_genre_scripts_to_randomly_remove,genre='Drama')
      Dramascripts = parser.get_all_scripts()
      while not(set([item[0] for item in allscripts]).isdisjoint(set([item[0] for item in Dramascripts]))):
         toRemove = sample(Dramascripts, n_genre_scripts_to_randomly_remove)
         Dramascripts = [e for e in Dramascripts if e not in toRemove]

      parser = IMSDBScraper(n_scripts=n_genre_scripts_to_add+n_genre_scripts_to_randomly_remove,genre='Film-Noir')
      Filmnoirscripts = parser.get_all_scripts()
      while not(set([item[0] for item in allscripts]).isdisjoint(set([item[0] for item in Filmnoirscripts]))):
         toRemove = sample(Filmnoirscripts, n_genre_scripts_to_randomly_remove)
         Filmnoirscripts = [e for e in Filmnoirscripts if e not in toRemove]

      parser = IMSDBScraper(n_scripts=n_genre_scripts_to_add+n_genre_scripts_to_randomly_remove,genre='Mystery')
      Mysteryscripts = parser.get_all_scripts()
      while not(set([item[0] for item in allscripts]).isdisjoint(set([item[0] for item in Mysteryscripts]))):
         toRemove = sample(Mysteryscripts, n_genre_scripts_to_randomly_remove)
         Mysteryscripts = [e for e in Mysteryscripts if e not in toRemove]

      parser = IMSDBScraper(n_scripts=n_genre_scripts_to_add+n_genre_scripts_to_randomly_remove,genre='Short')
      Shortscripts = parser.get_all_scripts()
      while not(set([item[0] for item in allscripts]).isdisjoint(set([item[0] for item in Shortscripts]))):
         toRemove = sample(Shortscripts, n_genre_scripts_to_randomly_remove)
         Shortscripts = [e for e in Shortscripts if e not in toRemove]

      parser = IMSDBScraper(n_scripts=n_genre_scripts_to_add+n_genre_scripts_to_randomly_remove,genre='Western')
      Westernscripts = parser.get_all_scripts()
      while not(set([item[0] for item in allscripts]).isdisjoint(set([item[0] for item in Westernscripts]))):
         toRemove = sample(Westernscripts, n_genre_scripts_to_randomly_remove)
         Westernscripts = [e for e in Westernscripts if e not in toRemove]

      genrescripts = {"Action": Actionscripts, "Comedy": Comedyscripts, "Family": Familyscripts, \
      "Horror": Horrorscripts, "Romance":Romancescripts, "Thriller":Thrillerscripts, \
      "Adventure":Adventurescripts, "Crime":Crimescripts, "Fantasy":Fantasyscripts, \
      "Musical":Musicalscripts, "Sci-Fi":Scifiscripts, "War":Warscripts, "Animation":Animationscripts, \
      "Drama":Dramascripts, "Film-Noir":Filmnoirscripts, "Mystery":Mysteryscripts, "Short":Shortscripts, "Western":Westernscripts}
      return [allscripts, genrescripts]
