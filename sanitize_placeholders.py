import re
import sys
from bs4 import BeautifulSoup

BRAND_PATTERNS = [
    r"kwality\s*wall's",
    r"amul",
    r"havmor",
    r"vadilal",
    r"mother\s*dairy",
    r"baskin\s*robbins",
    r"creambell",
    r"dinshaw's",
    r"arun",
    r"top\s*n\s*town",
    r"coolberg",
]

NUM_PATTERN = re.compile(r"\d+(?:\.\d+)?%?")
BRAND_REGEX = re.compile("|".join(BRAND_PATTERNS), re.IGNORECASE)


def sanitize_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')

    changed = False

    for elem in soup.find_all(string=True):
        # Skip style or script tag contents
        if elem.parent.name in ['style', 'script']:
            continue
        text = str(elem)
        new_text = NUM_PATTERN.sub('<VALUE>', text)
        new_text = BRAND_REGEX.sub('<BRAND>', new_text)
        if new_text != text:
            elem.replace_with(new_text)
            changed = True

    if changed:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(str(soup))

if __name__ == '__main__':
    for p in sys.argv[1:]:
        sanitize_file(p)
