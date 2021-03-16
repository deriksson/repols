def quote(field):
    return f'"{field}"' if "," in field else field
