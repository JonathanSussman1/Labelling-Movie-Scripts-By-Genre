import xml.etree.cElementTree as ET
from lxml import etree
import numpy as np
from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
import ssl



class IMSDBScraper:

    def __init__(self, n_scripts=10):
        """Constructor of the IMSDBParser class
        Args:
            n_scripts: number of scripts to be scraped (default:10)
        Raises:
            IOError: if one of the movies isn't found
        """
        # self.htmlParser = etree.HTMLParser()
        self.scripts = self.load_scripts(n_scripts)

    def load_scripts(self, n_scripts):
        """Load scripts from the IMSDB
        Args:
            n_scripts: number of scripts to be scraped (default:10)
        Returns:
            A list of parsed scripts
        """
        scripts = []
        res = requests.get("http://www.imsdb.com/all%20scripts/")
        parser = etree.XMLParser(recover=True)
        all_scripts = ET.fromstring(requests.get("http://www.imsdb.com/all%20scripts/").text, parser=parser) #this webpage contains all the scripts from IMSDB
        all_script_urls = all_scripts.xpath("//p/a")[:n_scripts]  # loads the first "n_scripts" scripts from the IMSDB
        for u in all_script_urls:
            title = u.text.replace(" ", "-") + ".html"
            try:
                movie_title="http://www.imsdb.com/scripts/" + title
                script = ET.fromstring(requests.get(movie_title).text, parser=parser).xpath("//pre/b")
            except IOError:  # movie not found
                continue
            # load list of all <b> tags
            btags = [speaker.text for speaker in script if speaker.text is not None and speaker.text.strip() != ""]
            if len(btags) > 50:  # the movie contains a reasonable number of lines
                name_column_indent = self.find_name_column(btags) #of all the b tags, find which ones represent actors
                script = self.parse_script(movie_title, name_column_indent)
                if len(script) > 0:  # correct parsing
                    scripts.append(script)
        return scripts

    def find_name_column(self, btags):
        """Find the indentation column containing characters' names
        Args:
            btags: a list of <b> tags from the script
        Returns:
           The number of spaces before the speakers' column
        """
        columns = {}
        for btag in btags:  # build an array mapping column_indent to its values
            leading_spaces = len(btag)-len(btag.lstrip())
            if columns.get(leading_spaces, None) is None:
                columns[leading_spaces] = []
            columns[leading_spaces].append(btag.strip().lower())
        names_occurrences = [[k for k in columns[c]] for c in columns]
        column = np.argmax([len(n) for n in names_occurrences])
        ck = list(columns.keys())
        return ck[column]

    @staticmethod
    def parse_script(uri, name_indent):
        """Parse an IMSDB script and turn it into a list of tuples
        Args:
            uri: the URI of the script to parse
            name_indent: the indentation of the speakers' column for this script
        Returns:
            A parsed script
        """
        script = []
        ssl._create_default_https_context = ssl._create_unverified_context
        soup = BeautifulSoup(urlopen(uri), 'html.parser')
        webpage = soup.find('pre').get_text().split("\n")  # scripts are wrapped in the <pre> tag
        textlines = []  # find the indentation of the column containing characters' lines
        for (i, l) in enumerate(webpage):
            if len(webpage[i-1]) - len(webpage[i-1].lstrip()) == name_indent and not(webpage[i].strip().startswith("(")):
                textlines.append((len(webpage[i]) - len(webpage[i].lstrip())))
        if len(textlines)==0:  # no text found: possibly an unknown annotation
            return []
        text_indent = textlines[-1]  # avoid first rows as they may contain noise
        name = ""  # speaker
        text = ""  # utterance
        for line in webpage:
            indent = len(line)-len(line.lstrip())
            if indent == name_indent:
                name = line.strip().lower()
            elif indent == text_indent:
                text += " " + line.strip()
            else:
                if name != "" and text != "":
                    script.append((name, text))
                    text = ""
        return script

    def get_all_scripts(self):
        """Get list of parsed scripts
        Returns:
            A list of parsed scripts
        """
        return self.scripts