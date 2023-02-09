def encode_to_utf8(string):
    """Encodes a latin1 string to utf-8"""
    if string:
        return string.encode('latin1').decode('utf-8')
    else:
        return None