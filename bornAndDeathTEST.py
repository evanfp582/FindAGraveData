#! python3

import re, pyperclip

#Create a regex for phone numner


text="""Esther A. Serfass Altemose 3 Feb 1899 – unknown
100591594
 Floyd C. Altemose
Floyd C. Altemose 11 Jul 1902 – 31 Dec 1976
Esther A. Serfass Altemose unknown – 1975
Esther A. Serfass Altemose 3 Feb 1899 – unknown
Esther A. Serfass Altemose 1899 – unknown
Eser A. Serfose unknown – 3 Feb 1975"""

preString= re.sub(
"(unknown – \w \w+ \d\d\d\d)|(([0-9]+\s\w\w\w\s[0-9][0-9][0-9][0-9]|([0-9][0-9][0-9][0-9]\s–)|(\s[0-9][0-9][0-9][0-9])$) – unknown)|unknown – \w+|(\w+ – unknown)"
," ",text)


print(preString)
