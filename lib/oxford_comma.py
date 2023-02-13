def oxford_comma(items):
    combo = ""
    if len(items) >= 3:
        last = items.pop()
        combo = ", ".join(items)
        combo += f", and {last}"
    elif len(items) == 2:
        combo = items[0] + " and " + items[1]
    else:
        combo = items.pop()
    return combo
