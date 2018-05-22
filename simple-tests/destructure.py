def destructure(dct, *keys):
    return (dct[key] for key in keys)
