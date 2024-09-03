"""List datatype sorting"""
def my_rank(e):
    """Sort the list"""
    print(e)
    return e[1]

rank = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41.0],
        ['Harsh', 39.0]]

rank.sort(key=my_rank)
