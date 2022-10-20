import unicodedata


def x(c):
            digit = f'{ord(c):x}'
            name = unicodedata.name(c, 'Name not found.')
            return f'\\U{digit:>08}: {name} - {c} \N{EM DASH} http://www.fileformat.info/info/unicode/char/%7Bdigit%7D'

print(x("~"))
