
import os
import re

COLORS = {
    "Machine": {
        # from iterm:
        "2d2a2e": "273136", # black
        "ff6188": "ff6d7e", # red
        "a9dc76": "a2e57b", # green
        "ffd866": "ffed72", # yellow
        "fc9867": "ffb270", # blue (orange)
        "ab9df2": "baa0f8", # magenta
        "78dce8": "7cd5f1", # cyan
        "fcfcfa": "f2fffc", # white
        "727072": "6b7678", # bright
        "5b595c": "545f62", # selection
        # from sublime:
        "221F22": "1d2528", # sidebar
        "373438": "2f393d", # caret row
        "403E41": "3a4449", # command bg
        "939293": "798384", # inactive icons
    },
    "Octagon": {
        # from iterm:
        "2d2a2e": "282a3a", # black
        "ff6188": "ff657a", # red
        "a9dc76": "bad761", # green
        "ffd866": "ffd76d", # yellow
        "fc9867": "ff9b5e", # blue (orange)
        "ab9df2": "c39ac9", # magenta
        "78dce8": "9cd1bb", # cyan
        "fcfcfa": "eaf2f1", # white
        "727072": "696d77", # bright
        "5b595c": "535763", # selection
        # from sublime:
        "221F22": "1e1f2b", # sidebar
        "373438": "2e3140", # caret row
        "403E41": "3a3d4b", # command bg
        "939293": "767b81", # inactive icons
    },
    "Ristretto": {
        # from iterm:
        "2d2a2e": "2c2525", # black
        "ff6188": "fd6883", # red
        "a9dc76": "adda78", # green
        "ffd866": "f9cc6c", # yellow
        "fc9867": "f38d70", # blue (orange)
        "ab9df2": "a8a9eb", # magenta
        "78dce8": "85dacc", # cyan
        "fcfcfa": "fff1f3", # white
        "727072": "72696a", # bright
        "5b595c": "5b5353", # selection
        # from sublime:
        "221F22": "211c1c", # sidebar
        "373438": "332c2c", # caret row
        "403E41": "403838", # command bg
        "939293": "8c8384", # inactive icons
    },
    "Spectrum": {
        # from iterm:
        "2d2a2e": "222222", # black
        "ff6188": "fc618d", # red
        "a9dc76": "7bd88f", # green
        "ffd866": "fce566", # yellow
        "fc9867": "fd9353", # blue (orange)
        "ab9df2": "948ae3", # magenta
        "78dce8": "5ad4e6", # cyan
        "fcfcfa": "f7f1ff", # white
        "727072": "69676c", # bright
        "5b595c": "525053", # selection
        # from sublime:
        "221F22": "191919", # sidebar
        "373438": "2c2c2c", # caret row
        "403E41": "363537", # command bg
        "939293": "8b888f", # inactive icons
    }
}

with open("src/Monokai Pro F.theme.json", "r") as f:
    default_theme = f.read()

with open("resources/themes/Monokai Pro F.xml", "r") as f:
    default_scheme = f.read()

for name, colors in COLORS.items():
    theme = default_theme
    scheme = default_scheme

    for k,v in colors.items():
        color = re.compile(re.escape(k), re.IGNORECASE)

        theme = color.sub(v, theme)
        scheme = color.sub(v, scheme)

    theme = theme.replace("Monokai Pro F.xml", "Monokai Pro F {name}.xml".format(name=name))
    theme = theme.replace("\"Monokai Pro F\"", "\"Monokai Pro F (Filter {name})\"".format(name=name))

    scheme = scheme.replace("Monokai Pro F", "Monokai Pro F (Filter {name})".format(name=name))

    with open("src/Monokai Pro F {name}.theme.json".format(name=name), "w") as f:
        f.write(theme)

    with open("resources/themes/Monokai Pro F {name}.xml".format(name=name), "w") as f:
        f.write(scheme)
