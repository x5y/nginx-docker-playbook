from bs4 import BeautifulSoup
from collections import Counter
import re
import sys

file_name = sys.argv[1]
fp = open(file_name)
contents = fp.read()

soup = BeautifulSoup(contents, features="html.parser")

body_strings = soup.body.strings

words = []

for string in body_strings:
    words = words + re.sub('\W+', ' ', string.lower()).split()

c = Counter(words)

print(c.most_common(1))
