# https://www.reddit.com/r/dailyprogrammer/comments/5seexn/20170206_challenge_302_easy_spelling_with/

elements = {
  "ac": "Actinium",
  "al": "Aluminum",
  "am": "Americium",
  "sb": "Antimony",
  "ar": "Argon",
  "as": "Arsenic",
  "at": "Astatine",
  "ba": "Barium",
  "bk": "Berkelium",
  "be": "Beryllium",
  "bi": "Bismuth",
  "b": "Boron",
  "br": "Bromine",
  "cd": "Cadmium",
  "ca": "Calcium",
  "cf": "Californium",
  "c": "Carbon",
  "ce": "Cerium",
  "cs": "Cesium",
  "cl": "Chlorine",
  "cr": "Chromium",
  "co": "Cobalt",
  "cu": "Copper",
  "cm": "Curium",
  "dy": "Dysprosium",
  "es": "Einsteinium",
  "er": "Erbium",
  "eu": "Europium",
  "fm": "Fermium",
  "f": "Fluorine",
  "fr": "Francium",
  "gd": "Gadolinium",
  "ga": "Gallium",
  "ge": "Germanium",
  "au": "Gold",
  "hf": "Hafnium",
  "he": "Helium",
  "ho": "Holmium",
  "h": "Hydrogen",
  "in": "Indium",
  "i": "Iodine",
  "ir": "Iridium",
  "fe": "Iron",
  "kr": "Krypton",
  "la": "Lanthanum",
  "lr": "Lawrencium",
  "pb": "Lead",
  "li": "Lithium",
  "lu": "Lutetium",
  "mg": "Magnesium",
  "mn": "Manganese",
  "md": "Mendelevium",
  "hg": "Mercury",
  "mo": "Molybdenum",
  "nd": "Neodymium",
  "ne": "Neon",
  "np": "Neptunium",
  "ni": "Nickel",
  "nb": "Niobium",
  "n": "Nitrogen",
  "no": "Nobelium",
  "os": "Osmium",
  "o": "Oxygen",
  "pd": "Palladium",
  "p": "Phosphorus",
  "pt": "Platinum",
  "pu": "Plutonium",
  "po": "Polonium",
  "k": "Potassium",
  "pr": "Praseodymium",
  "pm": "Promethium",
  "pa": "Protactinium",
  "ra": "Radium",
  "rn": "Radon",
  "re": "Rhenium",
  "rh": "Rhodium",
  "rb": "Rubidium",
  "ru": "Ruthenium",
  "rf": "Rutherfordium",
  "sm": "Samarium",
  "sc": "Scandium",
  "se": "Selenium",
  "si": "Silicon",
  "ag": "Silver",
  "na": "Sodium",
  "sr": "Strontium",
  "s": "Sulfur",
  "ta": "Tantalum",
  "tc": "Technetium",
  "te": "Tellurium",
  "tb": "Terbium",
  "tl": "Thallium",
  "th": "Thorium",
  "tm": "Thulium",
  "sn": "Tin",
  "ti": "Titanium",
  "w": "Tungsten",
  "u": "Uranium",
  "v": "Vanadium",
  "xe": "Xenon",
  "yb": "Ytterbium",
  "y": "Yttrium",
  "zn": "Zinc",
  "zr": "Zirconium"
}


def make_word(word):
    elements_in_word = []
    chars_matched = 0

    while True:
        for char in range(chars_matched + 1, len(word) + 1):
            w = word[chars_matched:char]

            if w in elements.keys():
                chars_matched += len(w)
                elements_in_word.append(elements[w])

        if len(word) == chars_matched:
            return elements_in_word


print(', '.join(x for x in make_word("sickness")))