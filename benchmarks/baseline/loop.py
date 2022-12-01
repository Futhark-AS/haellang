setup = """
def loop():
    i = 0
    while i<1_000_000:
        i+=1
    return i
"""

statement = 'loop()'