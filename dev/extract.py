def is_pa(line):
    """Check if a line has Perso-Arabic text in it."""
    letters =  set('ا ب ت ة ث ج ح خ د ذ ر ز س ش ص ض ط ظ ع غ ف ق ك ل م ن ه و ي ء آ أ ؤ إ ؤ'.split(" "))
    for letter in line:
        if letter in letters:
            return True
    return False

def get_defs(page):
    meaning = 'معنی'


if __name__ == "__main__":
    with open("scraped.txt", "r") as infile:
        for line in infile:
            if is_pa(line):
                print(line)
