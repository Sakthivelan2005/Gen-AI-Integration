def random(min, max):
    import time
    ns = time.time_ns()
    range = max - min + 1
    random_offset = ns % range
    return min + random_offset

print(random(7,10))