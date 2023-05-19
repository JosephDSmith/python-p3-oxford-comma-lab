def oxford_comma(items):
    if len(items) >=3:
        return ', '.join(items[0:-1]) + ', and ' + items[-1]
    elif len(items) ==2:
        return ' and '.join(items)
    elif len(items) ==1:
        return ''.join(items)
