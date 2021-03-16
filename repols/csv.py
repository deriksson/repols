def quote(field):
    return f'"{escape(field)}"' if "," in field or '"' in field else escape(field)


def escape(field: str):
    return field.replace('"', '""')
