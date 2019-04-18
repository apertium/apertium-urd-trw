import re
from collections import defaultdict


def is_pa(line):
    """Check if a line has Perso-Arabic text in it."""
    letters = set('ا ب ت ة ث ج ح خ د ذ ر ز س ش ص ض ط ظ ع غ ف ق ك ل م ن ه و ي ء آ أ ؤ إ ؤ'.split(" "))
    for letter in line:
        if letter in letters:
            return True
    return False


def get_defs(page):
    definitions = defaultdict(list)
    postags = {'صفت': ['adj'], 'اسم مونث': ['n', 'f'], 'اسم مذکر': ['n', 'm'], 'فعل متعلق': ['adv'],
               'فعل متعدی': ['v', 'tv'], 'فعل لازم': ['v', 'iv']}
    meaning = 'معنی'


def build_entry(left, leftfeats, right, rightfeats):
    start, mid, end = '<e><p><l>', '</l><r>', '</r></p></e>'
    out = start + left
    for item in leftfeats:
        out += '<s n="' + item + '"/>'
    out += mid + right
    for item in rightfeats:
        out += '<s n="' + item + '"/>'
    out += end
    return out


if __name__ == "__main__":
    with open("scraped.txt", "r") as infile:
        for line in infile:
            if is_pa(line):
                print(line)
