
def utf8_encode(unicode_str):
    return unicode_str.encode('utf-8')


def ascii_encode(unicode_str):
    try:
        return unicode_str.encode('ascii')
    except UnicodeEncodeError:
        return None


def is_ascii_encoded(bytes_str):
    try:
        bytes_str.decode('ascii')
        return True
    except UnicodeDecodeError:
        return False
